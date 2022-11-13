import app.devices


class Reader:
    device: app.devices.Device
    _reports = None

    def __init__(self, device: app.devices.Device):
        self.device = device
        self.initialize()

    def initialize(self):
        pass

    def get_report(self, number: int):
        return self.get_reports()[number - 1 if number > 0 else number]

    def get_reports(self):
        if self._reports is None:
            self._read_reports()
        return self._reports

    def _read_reports(self):
        raise NotImplementedError()
