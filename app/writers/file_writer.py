import os
import json
import app.config
from app.fields.array import ReportList
from app.writers import Writer


class FileWriter(Writer):
    def _check_if_exists(self):
        return os.path.isfile(self.destination)

    def _can_create_file(self):
        return not self._check_if_exists() or (self._check_if_exists() and app.config.overwrite)

    def write_reports(self, report_list: ReportList):
        if self._can_create_file():
            data = {}
            if app.config.as_bytes:
                data['reports'] = report_list.get_byte_value()
                data['format'] = 'bytes'
            else:
                data['reports'] = report_list.get_readable_value()
                data['format'] = 'readable'
            open(self.destination, 'w').write(json.dumps(data, indent=app.config.json_indent))
        else:
            raise Exception('File already exists and overwrite flag is false!')
