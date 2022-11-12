from app.readers.reader import Reader
import app.core
import devices


class DeviceReader(Reader):
    handler: app.core.DeviceHandler
    device: devices.Device

    def __init__(self, device: devices.Device):
        self.device = device
        self.handler = app.core.DeviceHandler(device)

    def t(self):
        import pprint
        pprint.pprint(self.handler.read_reports())
