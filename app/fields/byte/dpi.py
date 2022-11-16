from app.fields.byte import ByteField


class DPI(ByteField):

    def make_readable_value(self, byte):
        return int(byte) * 50

    def make_byte_value(self, readable):
        return int(readable) // 50
