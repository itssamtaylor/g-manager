import json
from app.readers.reader import Reader


class JsonReader(Reader):
    def _read_reports(self):
        self._reports = json.loads(open(self.source, 'r').read())
