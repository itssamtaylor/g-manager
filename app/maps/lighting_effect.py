from app.maps.static_map import StaticMap


class LightingEffectMap(StaticMap):
    _map = {
        0x00: "NO_EFFECT",
        0x01: "PULSE",
        0x02: "RAINBOW",
    }
