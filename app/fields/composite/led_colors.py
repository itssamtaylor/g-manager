import app.lang
from app.fields.byte import ByteField
from app.fields.composite import CompositeField


class LEDColors(CompositeField):
    _map = [
        ('red', ByteField),
        ('green', ByteField),
        ('blue', ByteField)
    ]
