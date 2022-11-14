from app.fields import Field
from app.fields.byte import ByteField


class ArrayField(Field):
    _field_type = ByteField
    _data = []

    def pre_init(self):
        self._field_type = self._field_type(self.device)

    def get_total_bytes(self):
        bytes_per_item = self._field_type.get_total_bytes()
        return bytes_per_item * len(self._data)

    def from_readable(self, readable):
        pass

    def from_byte(self, byte):
        self._data = [b for b in byte]
