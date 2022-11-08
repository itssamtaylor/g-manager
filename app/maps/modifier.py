from app.maps.static_map import StaticMap


class ModifierMap(StaticMap):
    _map: dict[int, str] = {
        0: "LCTRL",
        1: "LSHIFT",
        2: "LALT",
        3: "LGUI",
        4: "RCTRL",
        5: "RSHIFT",
        6: "RALT",
        7: "RGUI",
    }
