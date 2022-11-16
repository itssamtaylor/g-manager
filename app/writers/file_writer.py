import os

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
            open(self.destination, 'w').write(report_list.to_json())
        else:
            raise Exception('File already exists and overwrite flag is false!')
