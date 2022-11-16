import app.devices
from app.core import DeviceHandler
from app.fields.array import ReportList
from app.writers import Writer


class DeviceWriter(Writer):
    handler: DeviceHandler

    def initialize(self):
        if not isinstance(self.destination, app.devices.Device):
            raise TypeError(self.__class__.__name__ + ' expects destination to be of type Device!')
        self.handler = DeviceHandler(self.destination)

    def _validate(self, report_list: ReportList):
        assert len(self.destination.report_ids) == len(report_list.get_readable_value())
        for report_id, report in zip(self.destination.report_ids, report_list.get_items()):
            assert report_id == report.get_readable_value()['reportId']
            assert self.destination.report_length == report.get_total_bytes()

    def _write(self, report_list: ReportList):
        if not app.config.dry_run:
            self.handler.write_reports(report_list.get_items())

    def write_reports(self, report_list: ReportList):
        if not app.config.force:
            self._validate(report_list)
        self._write(report_list)
