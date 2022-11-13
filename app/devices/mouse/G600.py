from app.devices.mouse import Mouse
from app.fields.byte import PollRate
from app.fields.composite import ButtonMap, DPIGroup, LEDColors, LightingType, Unknown


class G600(Mouse):
    product_id = 0xc24a
    control_interface = 1
    report_ids = (0x03f3, 0x03f4, 0x03f5)
    report_length = 154
    num_buttons = 20
    shiftable = True
    has_dpi_shift = True
    unknown_group_indexes = (
        (0x46, 0x4b),
        (0x52, 0x5f),
    )

    report_map = (
        ('ledColors', LEDColors),
        ('lightingType', LightingType),
        ('unknown', Unknown),
        ('pollRate', PollRate),
        ('dpiGroup', DPIGroup),
        ('unknown', Unknown),
        ('buttonMap', ButtonMap),
        ('ledColorsShifted', LEDColors),
        ('buttonMapShifted', ButtonMap),
    )

    button_names = (
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
    )
