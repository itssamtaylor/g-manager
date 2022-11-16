import json

import app.config
from app.fields.array import ReportList
from app.readers.reader import Reader


class FileReader(Reader):
    def _read_reports(self):
        self._report_list = ReportList(app.config.get_device())
        data = json.loads(open(self.source, 'r').read())

        if 'format' not in data:
            raise Exception('format key not found in file!')

        if 'reports' not in data:
            raise Exception('reports key not found in file!')

        if data['format'] == 'bytes':
            self._report_list.load_byte_value(data['reports'])
        else:
            self._report_list.load_readable_value(data['reports'])

        return self._report_list
