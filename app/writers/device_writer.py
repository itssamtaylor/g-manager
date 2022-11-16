import app.devices
from app.core import DeviceHandler
from app.fields.array import ReportList
from app.writers import Writer
import app.core


class DeviceWriter(Writer):
    handler: DeviceHandler

    def initialize(self):
        if not isinstance(self.destination, app.devices.Device):
            raise TypeError(self.__class__.__name__ + ' expects destination to be of type Device!')
        self.handler = DeviceHandler(self.destination)

    def _validate(self, report_list: ReportList):
        app.core.verbose('Validating reports: ', end='')
        assert len(self.destination.report_ids) == len(report_list.get_readable_value())
        for report_id, report in zip(self.destination.report_ids, report_list.get_items()):
            assert report_id == report.get_readable_value()['reportId']
            assert self.destination.report_length == report.get_total_bytes()
        app.core.verbose('[PASSED]', prefix=False)

    def _write(self, report_list: ReportList):
        if not app.config.dry_run:
            app.core.info('Writing to device: ', end='')
            success = self.handler.write_reports(report_list.get_items())
            app.core.info('[SUCCESS]' if success else '[FAIL]', prefix=False)
        else:
            app.core.info('Dry-run flag enabled, will not write to device.')

    def write_reports(self, report_list: ReportList):
        if not app.config.force:
            self._validate(report_list)
        else:
            app.core.info('Force flag enabled, skipping validation.')
        self._write(report_list)
