from app.fields.byte import ByteField


class PollRate(ByteField):

    def make_readable_value(self, byte):
        return 1000 // (1 + int(byte))

    def make_byte_value(self, readable):
        return (1000 // int(readable)) - 1
