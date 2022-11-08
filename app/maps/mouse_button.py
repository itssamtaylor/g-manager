from app.maps.static_map import StaticMap


class MouseButtonMap(StaticMap):
    _map = {
        0x00: "NO_MOUSEBUT",
        0x01: "LEFT_CLICK",
        0x02: "RIGHT_CLICK",
        0x03: "MIDDLE_CLICK",
        0x04: "BACK",
        0x05: "FORWARD",
        0x06: "MOUSE6",
        0x07: "MOUSE7",
        0x11: "DPI_UP",
        0x12: "DPI_DOWN",
        0x13: "DPI_CYCLING",
        0x14: "MODE_SWITCH",
        0x15: "DPI_SHIFT",
        0x16: "DPI_DEFAULT",
        0x17: "GSHIFT",
    }
