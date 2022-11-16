from array import array

from app.fields import Field


class ByteField(Field):

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
        self._byte_value = byte

    def _set_readable_value(self, readable):
        self._readable_value = readable

    def load_byte_value(self, byte):
        if isinstance(byte, list | tuple | array | bytearray):
            if len(byte) == 1:
                byte = byte[0]
            else:
                raise ValueError('byte should be an integer or array with one item')
        self._set_byte_value(byte)
        try:
            self._set_readable_value(self.make_readable_value(byte))
        except NotImplementedError:
            self._set_readable_value(byte)
        return self

    def load_readable_value(self, readable):
        self._set_readable_value(readable)
        try:
            self._set_byte_value(self.make_byte_value(readable))
        except NotImplementedError:
            self._set_byte_value(readable)
        return self
