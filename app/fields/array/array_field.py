from app.fields import Field
from app.fields.byte import ByteField


class ArrayField(Field):
    _field_type = ByteField
    _length = 0

    def pre_init(self):
        self._field_type = self._field_type(self.device)

    def get_total_bytes(self):
        bytes_per_item = self._field_type.get_total_bytes()
        return bytes_per_item * self._length

    def load_readable_value(self, readable):
        pass

    def load_byte_value(self, byte):
        self._byte_value = byte
        self._readable_value = []
        for b in byte:
            self._field_type.load_byte_value(b)
            self._readable_value.append(self._field_type.readable_value)
        return self
