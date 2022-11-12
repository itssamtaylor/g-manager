import app


class DPIGroup(app.types.composite.Composite):
    _map = [
        (app.lang.get('dpi_group.dpi_shift_dpi'), app.types.byte.DPI),
        (app.lang.get('dpi_group.default_index'), app.types.byte.Byte),
    ]

    def initialize(self):
        for index in range(1, app.config.get_device().num_dpi_options):
            self._map.append(
                (app.lang.replace('dpi_group.dpi_item', ('index', index)), app.types.byte.DPI)
            )
