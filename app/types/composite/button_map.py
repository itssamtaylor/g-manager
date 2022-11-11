import app.types.composite.button_action as action
from app.types.composite import Composite


class ButtonMap(Composite):
    _map = []

    def __init__(self):
        if len(self._map) is 0:
            for i in range(1, super().config.device.num_buttons):
                self._map.append(('g' + str(i), action.ButtonAction))

