import config, app


class ButtonMap(app.types.composite.Composite):
    _map = []

    def initialize(self):
        if len(self._map) is 0:
            if callable(getattr(self.device, 'button_names')) and self.device.button_names() is not None:
                self._map = self.device.button_names()
            else:
                for i in range(1, config.get_device().num_buttons):
                    self._map.append((app.lang.get('button_map.prefix') + str(i), app.types.composite.ButtonAction))
