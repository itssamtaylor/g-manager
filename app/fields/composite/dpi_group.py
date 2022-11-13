import app.config
import app.lang
from app.fields.byte import ByteField, DPI
from app.fields.composite import CompositeField


class DPIGroup(CompositeField):
    _map = [
        ('dpiShiftDpi', DPI),
        ('defaultDpiIndex', ByteField),
    ]

    def initialize(self):
        for index in range(1, app.config.get_device().num_dpi_options):
            self._map.append(
                ('dpi' + str(index), DPI)
            )
