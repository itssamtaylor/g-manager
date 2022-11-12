import demandimport
import typing
import json
import config

with demandimport.enabled():
    pass


class Type(object):
    _shifted: bool = False
    _dict: dict[str | int, typing.Any] = {}
    device = None

    def __init__(self, device, **kwargs):
        self.device = device
        self._shifted = kwargs.get('shifted') or False
        self.initialize()

    def initialize(self):
        pass

    def from_json(self, json_string: str):
        self._dict = json.loads(json_string)

    def to_json(self):
        return json.dumps(self._dict, indent=config.json_indent)
