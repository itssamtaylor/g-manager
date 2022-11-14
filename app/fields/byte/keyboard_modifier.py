from app.fields.byte import ByteField
from app.maps import ModifierMap


class KeyboardModifier(ByteField):
    _modifier_map = ModifierMap()

    def make_readable_value(self, byte):
        codes = []
        for index, bit in enumerate(reversed('{:08b}'.format(byte))):
            if bit == '1':
                codes.append(self._modifier_map.from_byte(index))
        readable = '+'.join(codes)
        return readable if readable != '' else 'NO_MOD'

    def make_byte_value(self, readable):
        readable = str(readable).strip().upper()
        byte = 0
        if readable == 'NO_MOD':
            return byte

        for code in readable.split('+'):
            modifier = self._modifier_map.from_string(code)
            byte += 2 ** modifier if modifier is not None else 0

        return byte
