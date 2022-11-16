import os
import json
import app.config
import app.core
from app.fields.array import ReportList
from app.writers import Writer


class FileWriter(Writer):
    def _check_if_exists(self):
        exists = os.path.isfile(self.destination)
        app.core.verbose('File already exists: {}'.format('YES' if exists else 'NO'))
        return exists

    def _can_create_file(self):
        exists = self._check_if_exists()
        return not exists or (exists and app.config.overwrite)

    def write_reports(self, report_list: ReportList):
        if self._can_create_file():
            data = {}
            if app.config.as_bytes:
                data['reports'] = report_list.get_byte_value()
                data['format'] = 'bytes'
            else:
                data['reports'] = report_list.get_readable_value()
                data['format'] = 'readable'
            app.core.info('Writing to file "{}"...'.format(self.destination), end='')
            open(self.destination, 'w').write(json.dumps(data, indent=app.config.json_indent))
            app.core.info('SUCCESS')
        else:
            raise Exception('File already exists and overwrite flag is false!')
