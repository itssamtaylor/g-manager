import app.config
import app.lang
from app.types.composite import Composite, ButtonAction


class ButtonMap(Composite):
    _map = []

    def initialize(self):
        if len(self._map) is 0:
            if callable(getattr(self.device, 'button_names')) and self.device.button_names() is not None:
                self._map = self.device.button_names()
            else:
                for i in range(1, app.config.get_device().num_buttons):
                    self._map.append((app.lang.get('button_map.prefix') + str(i), ButtonAction))
