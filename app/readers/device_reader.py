import app.core
import app.devices
from app.fields.composite import Report
from app.readers.reader import Reader
import app.config


class DeviceReader(Reader):
    handler: app.core.DeviceHandler

    def initialize(self):
        if not isinstance(self.source, app.devices.Device):
            raise TypeError(self.__class__.__name__ + ' expects source to be a device!')
        self.handler = app.core.DeviceHandler(self.source)

    def _read_reports(self):
        self._reports = []
        for report in self.handler.read_reports():
            self._reports.append(Report(app.config.get_device()).load_byte_value(report))
        return self._reports
