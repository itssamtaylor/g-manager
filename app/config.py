import toml
import typing
import app.helpers

_loaded = toml.load('config.toml')


def get(keys: str, default: typing.Any = None):
    value = app.helpers.get_from_dict(keys, _loaded)
    return value or default


def get_device():
    import devices
    return devices.load_device(get('device.name'), get('device.type', 'mouse'))


# App config
debug = get('app.debug', False)
force = get('app.force', False)
json_indent = get('app.json_indent', 4)
