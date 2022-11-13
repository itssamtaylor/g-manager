import time

import usb.core
import usb.util

import app.devices


class DeviceHandler:
    device_class: app.devices.Device
    device: usb.core.Device
    _disconnected_from_system = False
    _claimed = False
    _auto_connections = True
    _in_batch_job = False

    def __init__(self, device: app.devices.Device):
        self.device_class = device
        self.device = usb.core.find(idVendor=self.device_class.vendor_id, idProduct=self.device_class.product_id)

    def set_auto(self):
        self._auto_connections = True

    def set_manual(self):
        self._auto_connections = False

    def _handle_connection(self):
        if self._auto_connections and not self._in_batch_job:
            self.connect()

    def _handle_disconnection(self):
        if self._auto_connections and not self._in_batch_job:
            self.disconnect()

    def open_batch_job(self):
        self._handle_connection()
        self._in_batch_job = True

    def close_batch_job(self):
        self._in_batch_job = False
        self._handle_disconnection()

    def is_kernel_connected(self):
        return self.device.is_kernel_driver_active(self.device_class.control_interface)

    def is_connected(self):
        return self._disconnected_from_system and self._claimed

    def disconnect_system(self):
        self.device.detach_kernel_driver(self.device_class.control_interface)
        self._disconnected_from_system = True

    def reconnect_system(self):
        self.device.attach_kernel_driver(self.device_class.control_interface)
        self._disconnected_from_system = False

    def claim(self):
        usb.util.claim_interface(self.device, self.device_class.control_interface)
        self._claimed = True

    def release(self):
        usb.util.release_interface(self.device, self.device_class.control_interface)
        self._claimed = False

    def disconnect(self):
        if self.is_connected():
            self.release()
            self.reconnect_system()

    def connect(self):
        if not self.is_connected():
            self.disconnect_system()
            self.claim()

    def ctrl_transfer(self, *args, **kwargs):
        self._handle_connection()
        data = self.device.ctrl_transfer(*args, **kwargs)
        self._handle_disconnection()
        return data

    def read_report(self, report_id: int, length: int):
        return self.ctrl_transfer(
            bmRequestType=self.device_class.hid_read_type,
            bRequest=self.device_class.hid_read_request,
            wValue=report_id,
            wIndex=self.device_class.hid_read_index,
            data_or_wLength=length,
            timeout=self.device_class.hid_timeout
        )

    def write_report(self, report_id: int, data: bytes):
        return self.ctrl_transfer(
            bmRequestType=self.device_class.hid_write_type,
            bRequest=self.device_class.hid_write_request,
            wValue=report_id,
            wIndex=self.device_class.hid_write_index,
            data_or_wLength=data,
            timeout=self.device_class.hid_timeout
        )

    def read_reports(self):
        self.open_batch_job()
        reports = []
        for report_id in self.device_class.report_ids:
            reports.append(self.read_report(report_id, self.device_class.report_length))
        self.close_batch_job()
        return reports

    def write_reports(self, reports: list):
        self.open_batch_job()
        success = True
        for report_id, report in zip(self.device_class.report_ids, reports):
            length = self.write_report(report_id, report)
            success &= length == len(report)
            time.sleep(1.1)
        self.close_batch_job()
        return success
