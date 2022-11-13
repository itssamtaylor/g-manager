import app.lang
from app.fields.composite import CompositeField


class ButtonAction(CompositeField):
    _map = [
        (app.lang.get('button_action.device_scan_code'), None),
        (app.lang.get('button_action.kb_modifier'), None),
        (app.lang.get('button_action.kb_scan_code'), None),
    ]
