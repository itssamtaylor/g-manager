class StaticMap:
    _map: dict[int, str] = {}
    _flipped: dict[str, int] = {}

    def __init__(self):
        self._flipped = {v: k for k, v in self._map.items()}

    def all(self) -> dict[int, str]:
        return self._map

    def flipped(self) -> dict[str, int]:
        return self._flipped

    def get(self, search: str | int) -> int | str | None:
        try:
            if isinstance(search, str):
                return self.to_byte(search)
            else:
                return self.to_string(search)
        except KeyError:
            return None

    def from_byte(self, raw: int) -> str:
        return self.to_string(raw)

    def from_string(self, string: str) -> int:
        return self.to_byte(string)

    def to_string(self, raw: int) -> str:
        return self._map[raw]

    def to_byte(self, string: str) -> int:
        return self._flipped[string.strip().upper()]
