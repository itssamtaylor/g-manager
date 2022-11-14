import app.lang
from app.fields.byte import ByteField
from app.fields.composite import CompositeField


class LightingType(CompositeField):
    composition_map = [
        ('lightingEffect', ByteField),
        ('lightingChangeRate', ByteField),
    ]
