from app.maps.key_map import KeyMap
from app.maps.lighting_effect_map import LightingEffectMap
from app.maps.modifier_map import ModifierMap
from app.maps.mouse_button_map import MouseButtonMap


def key_map() -> KeyMap:
    return KeyMap()


def lighting_effect_map() -> LightingEffectMap:
    return LightingEffectMap()


def modifier_map() -> ModifierMap:
    return ModifierMap()


def mouse_button_map() -> MouseButtonMap:
    return MouseButtonMap()


def get_key(search: str | int) -> str | int | None:
    return key_map().get(search)


def get_lighting_effect(search: str | int) -> str | int | None:
    return lighting_effect_map().get(search)


def get_modifier(search: str | int) -> str | int | None:
    return modifier_map().get(search)


def get_mouse_button(search: str | int) -> str | int | None:
    return mouse_button_map().get(search)
