import app.devices
from app.fields.array import ReportList


class Writer:
    destination: app.devices.Device | str = None

    def __init__(self, destination: app.devices.Device | str):
        self.destination = destination
        self.initialize()

    def initialize(self):
        pass

    def write_reports(self, report_list: ReportList):
        raise NotImplementedError()
