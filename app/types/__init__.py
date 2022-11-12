import json
import app.config
import app.types.composite
import app.types.byte
from typing import Any


class Type(object):
    _shifted: bool = False
    _dict: dict[str | int, Any] = {}
    config = app.config

    def __init__(self, **kwargs):
        self.initialize()
        self._shifted = kwargs.get('shifted') or False

    def initialize(self):
        pass

    def from_json(self, json_string: str):
        self._dict = json.loads(json_string)

    def to_json(self):
        return json.dumps(self._dict, indent=self.config.json_indent)
