import app.core
import app.devices
from app.readers.reader import Reader


class DeviceReader(Reader):
    handler: app.core.DeviceHandler

    def initialize(self):
        self.handler = app.core.DeviceHandler(self.device)

    def _read_reports(self):
        self._reports = self.handler.read_reports()
        return self._reports
