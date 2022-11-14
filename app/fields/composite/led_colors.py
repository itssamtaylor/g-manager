import app.lang
from app.fields.byte import ByteField
from app.fields.composite import CompositeField


class LEDColors(CompositeField):
    composition_map = [
        ('red', ByteField),
        ('green', ByteField),
        ('blue', ByteField)
    ]
