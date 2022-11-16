from app.fields import Field
from app.fields.byte import ByteField


class ArrayField(Field):
    _field_type = ByteField
    _length = 0
    _items = []

    def pre_init(self):
        self._items = []
        self._field_type = self._field_type(self.device)

    def get_total_bytes(self):
        bytes_per_item = self._field_type.get_total_bytes()
        return bytes_per_item * self._length

    def load_readable_value(self, readable):
        self._items = []
        self._readable_value = readable
        self._byte_value = []
        for r in readable:
            instance = self._field_type.__class__(self.device)
            instance.load_readable_value(r)
            self._byte_value.append(instance.get_byte_value())
            self._items.append(instance)
        return self

    def load_byte_value(self, byte):
        self._items = []
        self._byte_value = byte
        self._readable_value = []
        for b in byte:
            instance = self._field_type.__class__(self.device)
            instance.load_byte_value(b)
            self._readable_value.append(instance.get_readable_value())
            self._items.append(instance)
        return self

    def get_items(self):
        return self._items
