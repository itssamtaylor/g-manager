class StaticMap:
    _map = {}
    _flipped = {}

    def __init__(self):
        self._flipped = {v: k for k, v in self._map.items()}

    def all(self):
        return self._map

    def flipped(self):
        return self._flipped

    def get(self, search):
        try:
            if isinstance(search, str):
                return self.to_raw(search)
            else:
                return self.to_string(search)
        except KeyError:
            return None

    def from_raw(self, raw):
        return self.to_string(raw)

    def from_string(self, string):
        return self.to_raw(string)

    def to_string(self, raw):
        return self._map[raw]

    def to_raw(self, string):
        return self._flipped[string.upper()]
