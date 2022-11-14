from app.fields.byte import ByteField, DPI
from app.fields.composite import CompositeField


class DPIGroup(CompositeField):
    composition_map = []

    def init(self):
        if self.device.has_dpi_shift:
            self.composition_map.append(('dpiShiftDpi', DPI))

        self.composition_map.append(('defaultDpiIndex', ByteField))

        for index in range(self.device.num_dpi_options):
            self.composition_map.append(
                ('dpi' + str(index + 1), DPI)
            )
