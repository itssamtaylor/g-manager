import typing

import toml

_loaded = toml.load('config.toml')
_device = None


def get(keys: str, default: typing.Any = None):
    import app.helpers
    value = app.helpers.get_from_dict(keys, _loaded)
    return value or default


def get_device():
    global _device
    if _device is None:
        import app.devices
        _device = app.devices.load_device(get('device.name'), get('device.type', 'mouse'))
    return _device


# App config
debug = get('app.debug', False)
force = get('app.force', False)
json_indent = get('app.json_indent', 4)
