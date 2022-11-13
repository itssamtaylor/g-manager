import app.lang
from app.fields.byte import ByteField
from app.fields.composite import CompositeField


class LightingType(CompositeField):
    _map = [
        ('lightingEffect', ByteField),
        ('lightingChangeRate', ByteField),
    ]
