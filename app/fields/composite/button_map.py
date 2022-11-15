import itertools

from app.fields.composite import CompositeField, ButtonAction


class ButtonMap(CompositeField):
    composition_map = []

    def init(self):
        if len(self.composition_map) == 0:
            if hasattr(self.device, 'button_names') and self.device.button_names is not None:
                self.composition_map = list(zip(self.device.button_names, itertools.repeat(ButtonAction)))
            else:
                for i in range(self.device.num_buttons):
                    self.composition_map.append(('g' + str(i + 1), ButtonAction))
