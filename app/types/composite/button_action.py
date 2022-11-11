from app.types.composite import Composite


class ButtonAction(Composite):
    _map = [
        ('deviceScanCode', None),
        ('kbModifiers', None),
        ('kbScanCode', None),
    ]
