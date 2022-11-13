import app.types.composite
import app.types.byte
from app.devices.mouse import Mouse


class G600(Mouse):
    product_id = 0xc24a
    control_interface = 1
    report_ids = (0x03f3, 0x03f4, 0x03f5)
    read_length = 154
    num_buttons = 20
    shiftable = True
    has_dpi_shift = True
    unknown_group_indexes = [(0x46, 0x4b), (0x52, 0x5f)]

    def map_report_to(self):
        return (
            app.types.composite.LEDColors(self),
            app.types.composite.LightingType(self),
            app.types.composite.Unknown(self),
            app.types.byte.PollRate(self),
            app.types.composite.DPIGroup(self),
            app.types.composite.Unknown(self),
            app.types.composite.ButtonMap(self),
            app.types.composite.LEDColors(self, shifted=True),
            app.types.composite.ButtonMap(self, shifted=True)
        )

    def button_names(self):
        return [
            'g1 (left button)',
            'g2 (right button)',
            'g3 (middle button)',
            'g4 (mousewheel left)',
            'g5 (mousewheel right)',
            'g6 (side/gshift)',
            'g7 (button back)',
            'g8 (button forward)',
            'g9 (side buttonpad)',
            'g10 (side buttonpad)',
            'g11 (side buttonpad)',
            'g12 (side buttonpad)',
            'g13 (side buttonpad)',
            'g14 (side buttonpad)',
            'g15 (side buttonpad)',
            'g16 (side buttonpad)',
            'g17 (side buttonpad)',
            'g18 (side buttonpad)',
            'g19 (side buttonpad)',
            'g20 (side buttonpad)',
        ]
