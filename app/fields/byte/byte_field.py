from app.fields import Field


class ByteField(Field):

    def get_total_bytes(self):
        return 1
