import collections

import app.lang


class Field(object):
    _dict = collections.OrderedDict()
    _shifted: bool = False
    _index = None
    device = None

    def __init__(self, device, **kwargs):
        self.device = device
        self._shifted = kwargs.get('shifted') or False
        self.initialize()

    def initialize(self):
        pass

    def test_data(self):
        return ''

    def _lang(self, key, **kwargs):
        return app.lang.replace(self.__class__.__name__ + '.' + key, **kwargs)

    def _name(self):
        return self._lang(
            '_name',
            shifted='shifted' if self._shifted else '',
            index=self._index or '',
            count_index='' if self._index is None else self._index + 1,
        )
