from app.fields import Field


class CompositeField(Field):
    composition_map: list = []
    _instance_map: list = []

    def post_init(self):
        self._instance_map = []
        for item in self.composition_map:
            if isinstance(item, tuple) and callable(item[1]):
                self._instance_map.append((item[0], item[1](self.device)))

    def get_total_bytes(self):
        total = 0
        for item in self._instance_map:
            total += item[1].get_total_bytes()
        return total
