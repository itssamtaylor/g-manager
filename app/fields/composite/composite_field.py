from app.fields import Field


class CompositeField(Field):
    _map = []

    def __init__(self, device, **kwargs):
        super().__init__(device, **kwargs)
        for index, item in enumerate(self._map):
            if isinstance(item, tuple) and callable(item[1]):
                self._map[index] = (item[0], item[1](self.device))

    def test_data(self):
        return self._map

