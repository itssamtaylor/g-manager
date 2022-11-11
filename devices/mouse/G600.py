import devices


class G600(devices.mouse.Mouse):
    product_id = 0xc24a
    control_interface = 1
    report_ids = (0x03f3, 0x03f4, 0x03f5)
    read_length = 154
    num_buttons = 20
    shiftable = True
    has_dpi_shift = True
    unknown_group_indexes = [(0x46, 0x4b), (0x52, 0x5f)]



