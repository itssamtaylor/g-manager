import app.lang
import app.types.composite.button_action as action
from app.types.composite import Composite


class ButtonMap(Composite):
    _map = []

    def __init__(self):
        if len(self._map) is 0:
            for i in range(1, super().config.device.num_buttons):
                self._map.append((app.lang.get('button_map.prefix') + str(i), action.ButtonAction))

