import app.devices
from app.fields.array import ReportList


class Reader:
    source: app.devices.Device | str = None
    _report_list: ReportList = None
    _read: bool = False

    def __init__(self, source: app.devices.Device | str):
        self._read = False
        self._report_list = ReportList(app.config.get_device())
        self.source = source
        self.initialize()

    def initialize(self):
        pass

    def get_reports(self):
        if not self._read:
            self._read_reports()
        return self._report_list

    def _read_reports(self):
        raise NotImplementedError()
