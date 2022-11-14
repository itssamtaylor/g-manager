import collections


class Field(object):
    _dict = collections.OrderedDict()
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

    def get_total_bytes(self):
        raise NotImplementedError()

    def get_arg(self, name, default=None):
        try:
            return self._kwargs[name]
        except KeyError:
            return default
