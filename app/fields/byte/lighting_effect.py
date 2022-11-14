from app.fields.byte import ByteField
from app.maps import LightingEffectMap


class LightingEffect(ByteField):
    _lighting_effect_map = LightingEffectMap()

    def make_readable_value(self, byte):
        return self._lighting_effect_map.from_byte(byte)

    def make_byte_value(self, readable):
        return self._lighting_effect_map.from_string(readable)
