from app.fields import Field


class ByteField(Field):
    byte_value = 0
    readable_value = None

    def get_total_bytes(self):
        return 1

    def make_readable_value(self, byte):
        raise NotImplementedError()

    def make_byte_value(self, readable):
        raise NotImplementedError()

    def _set_byte_value(self, byte):
        if byte < 0:
            byte = 0
        elif byte > 255:
            byte = 255
        self.byte_value = byte

    def _set_readable_value(self, readable):
        self.readable_value = readable

    def from_byte(self, byte):
        self._set_byte_value(byte)
        try:
            self._set_readable_value(self.make_readable_value(byte))
        except NotImplementedError:
            self._set_readable_value(byte)

    def from_readable(self, readable):
        self._set_readable_value(readable)
        try:
            self._set_byte_value(self.make_byte_value(readable))
        except NotImplementedError:
            self._set_byte_value(readable)
