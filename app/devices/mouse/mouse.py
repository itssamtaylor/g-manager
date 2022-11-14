from app.devices import Device
from app.fields.byte import DeviceButton, MouseButton

class Mouse(Device):
    num_buttons: int = 3
    num_dpi_options: int = 4
    has_dpi_shift: bool = False
    shiftable: bool = False
    button_names: tuple = None
    special_field_map = {
        DeviceButton: MouseButton
    }
