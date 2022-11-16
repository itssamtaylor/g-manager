import json

import app.config
from app.fields.array import ReportList
from app.readers.reader import Reader


class FileReader(Reader):
    def _read_reports(self):
        readable = json.loads(open(self.source, 'r').read())
        self._reports = ReportList(app.config.get_device()).load_readable_value(readable)
        return self._reports
