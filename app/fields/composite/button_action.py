from app.fields.byte.device_button import DeviceButton
from app.fields.byte.keyboard_button import KeyboardButton
from app.fields.byte.keyboard_modifier import KeyboardModifier
from app.fields.composite import CompositeField


class ButtonAction(CompositeField):
    _map = [
        ('deviceScanCode', DeviceButton),
        ('kbModifier', KeyboardModifier),
        ('kbScanCode', KeyboardButton),
    ]
