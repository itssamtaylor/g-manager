import json

import app.config


class Field(object):
    _byte_value = None
    _readable_value = None
    _kwargs = {}
    device = None

    def __init__(self, device, **kwargs):
        self.device = device
        self._kwargs = kwargs
        self.pre_init()
        self.init()
        self.post_init()

    def pre_init(self):
        pass

    def init(self):
        pass

    def post_init(self):
        pass

    def get_byte_value(self):
        return self._byte_value

    def get_readable_value(self):
        return self._readable_value

    def load_byte_value(self, byte):
        raise NotImplementedError()

    def load_readable_value(self, readable):
        raise NotImplementedError()

    def get_total_bytes(self):
        raise NotImplementedError()

    def get_arg(self, name, default=None):
        if name in self._kwargs:
            return self._kwargs[name]
        else:
            return default

    def __str__(self):
        return self.to_json()

    def to_json(self):
        return json.dumps(self.get_readable_value(), indent=app.config.json_indent)

    def from_json(self, json_string):
        return self.load_readable_value(json.loads(json_string))