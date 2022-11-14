from app.fields.byte import ByteField, LightingEffect
from app.fields.composite import CompositeField


class LightingType(CompositeField):
    composition_map = [
        ('lightingEffect', LightingEffect),
        ('lightingChangeRate', ByteField),
    ]
