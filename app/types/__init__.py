import json
import app.config
from typing import Any


class Type(object):
    _dict: dict[str | int, Any] = {}
    config = app.config

    def from_json(self, json_string: str):
        self._dict = json.loads(json_string)

    def to_json(self):
        return json.dumps(self._dict, indent=self.config.json_indent)

