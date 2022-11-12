import app.lang
from app.types.composite import Composite
from app.types.byte import Byte
from app.types.byte.dpi import DPI


class DPIGroup(Composite):
    _map = [
        (app.lang.get('dpi_group.dpi_shift_dpi'), DPI),
        (app.lang.get('dpi_group.default_index'), Byte),
    ]

    def __init__(self):
        for index in range(1, super().config.device.num_dpi_options):
            self._map.append(
                (app.lang.replace('dpi_group.dpi_item', ('index', index)), DPI)
            )

