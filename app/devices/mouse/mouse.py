from app.devices import Device


class Mouse(Device):
    num_buttons = 3
    num_dpi_options = 4
    has_dpi_shift = False
    shiftable = False

    def map_report_to(self):
        raise NotImplementedError()

    def button_names(self):
        return None
