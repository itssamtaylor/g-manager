from app.fields.byte import ByteField
from app.maps import MouseButtonMap


class MouseButton(ByteField):
    _mouse_map = MouseButtonMap()

    def make_readable_value(self, byte):
        return self._mouse_map.from_byte(byte)

    def make_byte_value(self, readable):
        return self._mouse_map.from_string(readable)
