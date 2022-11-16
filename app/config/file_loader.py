import json

import toml


class FileLoader:
    file_name: str
    file_type: str
    _loaded: dict = {}

    def __init__(self, file_name: str | None = None):
        self.file_name = file_name if file_name is not None else 'config.toml'
        self.file_type = self.file_name.split('.')[-1].lower()
        if hasattr(self, '_load_' + self.file_type) and callable(getattr(self, '_load_' + self.file_type)):
            self._loaded = getattr(self, '_load_' + self.file_type)()
        else:
            raise NotImplementedError(self.file_type + ' is an unsupported file type')

    def _load_toml(self):
        return toml.load(self.file_name)

    def _load_json(self):
        return json.load(open(self.file_name, 'r'))

    def get_loaded(self):
        return self._loaded
