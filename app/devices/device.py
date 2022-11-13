import app.config


class Device:
    hid_read_type: int = app.config.get('hid_defaults.hid_read_type')
    hid_read_request: int = app.config.get('hid_defaults.hid_read_request')
    hid_read_index: int = None
    hid_write_type: int = app.config.get('hid_defaults.hid_write_type')
    hid_write_request: int = app.config.get('hid_defaults.hid_write_request')
    hid_write_index: int = None
    hid_timeout: int = app.config.get('hid_defaults.hid_timeout')

    vendor_id: int = app.config.get('device_defaults.vendor_id')
    product_id: int = None
    control_interface: int = None

    report_ids: tuple = ()
    report_length: int = None
    report_map: tuple = None

    unknown_group_indexes: tuple = ()

    def __init__(self):
        self.num_unknown_groups = len(self.unknown_group_indexes)
        self.num_reports = len(self.report_ids)

        if self.hid_read_index is None:
            self.hid_read_index = self.control_interface

        if self.hid_write_index is None:
            self.hid_write_index = self.control_interface

    def get_report_map(self):
        if self.report_map is not None:
            return self.report_map
        else:
            raise NotImplementedError()
