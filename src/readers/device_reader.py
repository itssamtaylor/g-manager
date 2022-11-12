import devices, app
from readers.reader import Reader


class DeviceReader(Reader):
    handler: app.core.DeviceHandler
    device: devices.Device
    _reports = None

    def __init__(self, device: devices.Device):
        self.device = device
        self.handler = app.core.DeviceHandler(device)

    def read_reports(self):
        self._reports = self.handler.read_reports()
        return self._reports

    def get_reports(self):
        if self._reports is None:
            self.read_reports()
        return self._reports

    def get_report(self, number: int):
        return self.get_reports()[number if number > 0 else number - 1]

    def read_report(self, index_or_id: int):
        if index_or_id in self.device.report_ids:
            return self.handler.read_report(index_or_id, self.device.read_length)
        elif index_or_id < len(self.device.report_ids):
            return self.handler.read_report(self.device.report_ids[index_or_id], self.device.read_length)
        else:
            return None
