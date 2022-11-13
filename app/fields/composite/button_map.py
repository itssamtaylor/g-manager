import itertools
import app.config
import app.lang
from app.fields.composite import CompositeField, ButtonAction


class ButtonMap(CompositeField):
    _map = []

    def initialize(self):
        if len(self._map) == 0:
            if callable(getattr(self.device, 'button_names')) and self.device.button_names() is not None:
                self._map = list(zip(self.device.button_names(), itertools.repeat(ButtonAction)))
            else:
                for i in range(1, app.config.get_device().num_buttons):
                    self._map.append(('g' + str(i), ButtonAction))
