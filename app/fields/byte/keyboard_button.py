from app.fields.byte import ByteField
from app.maps import KeyMap


class KeyboardButton(ByteField):
    _key_map = KeyMap()

    def make_readable_value(self, byte):
        return self._key_map.from_byte(byte)

    def make_byte_value(self, readable):
        return self._key_map.from_string(readable)
