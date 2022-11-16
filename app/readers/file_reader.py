import json
import app.core
import app.config
from app.fields.array import ReportList
from app.readers.reader import Reader


class FileReader(Reader):
    def _read_reports(self):
        self._report_list = ReportList(app.config.get_device())

        app.core.verbose('Reading file: ', end='')
        data = json.loads(open(self.source, 'r').read())
        app.core.verbose('[SUCCESS]' if data is not None else '[FAIL]', prefix=False)

        version = data['version'] or ''

        if 'format' not in data:
            raise Exception('format key not found in file!')

        if 'reports' not in data:
            raise Exception('reports key not found in file!')

        if data['format'] == 'bytes':
            app.core.verbose('Importing bytes format from file.')
            self._report_list.load_byte_value(data['reports'])
        else:
            app.core.verbose('Importing readable format from file.')
            if version != app.version:
                app.core.warning('"{0}" was created using an older version of {1}.'.format(self.source, app.name))
                if not app.config.lenient:
                    raise Exception(
                        '"{0}" was created using an older version of {1} and lenient flag is disabled.'.format(
                            self.source, app.name)
                    )
            self._report_list.load_readable_value(data['reports'])

        return self._report_list
