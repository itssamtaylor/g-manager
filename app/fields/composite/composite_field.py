from array import array
from collections import OrderedDict

from app.fields import Field


def _name(obj):
    if isinstance(obj, tuple):
        return obj[0]
    return obj.__name__ if callable(obj) else obj.__class__.__name__


class CompositeField(Field):
    _byte_value = array('B')
    _readable_value = OrderedDict()
    composition_map: list = []
    _instance_map: list = []

    def _make_field_instance(self, obj):
        if callable(obj):
            if obj in self.device.special_field_map:
                return self.device.special_field_map[obj](self.device)
            else:
                return obj(self.device)
        else:
            return obj

    def post_init(self):
        self._byte_value = array('B')
        self._readable_value = OrderedDict()
        self._instance_map = []
        for item in self.composition_map:
            obj = item if not isinstance(item, tuple) else item[1]
            self._instance_map.append((
                _name(item),
                self._make_field_instance(obj)
            ))

    def get_total_bytes(self):
        total = 0
        for item in self._instance_map:
            total += item[1].get_total_bytes()
        return total

    def load_byte_value(self, byte):
        self._byte_value = byte
        byte_start = 0
        for instance in self._instance_map:
            byte_end = byte_start + instance[1].get_total_bytes()
            instance[1].load_byte_value(byte[byte_start:byte_end])
            self._readable_value[instance[0]] = instance[1].get_readable_value()
            byte_start = byte_end
        return self

    def load_readable_value(self, readable):
        pass
