class Field(object):
    byte_value = None
    readable_value = None
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

    def from_byte(self, byte):
        raise NotImplementedError()

    def from_readable(self, readable):
        raise NotImplementedError()

    def get_total_bytes(self):
        raise NotImplementedError()

    def get_arg(self, name, default=None):
        if name in self._kwargs:
            return self._kwargs[name]
        else:
            return default
