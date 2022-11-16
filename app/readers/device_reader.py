import app.core
import app.devices
from app.fields.array import ReportList
from app.readers.reader import Reader
import app.config


class DeviceReader(Reader):
    handler: app.core.DeviceHandler

    def initialize(self):
        if not isinstance(self.source, app.devices.Device):
            raise TypeError(self.__class__.__name__ + ' expects source to be a device!')
        self.handler = app.core.DeviceHandler(self.source)

    def _read_reports(self):
        self._report_list = ReportList(self.source).load_byte_value(self.handler.read_reports())
        return self._report_list
