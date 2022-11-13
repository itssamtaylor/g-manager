import toml
import typing

_loaded = toml.load('config.toml')


def get(keys: str, default: typing.Any = None):
    import app.helpers
    value = app.helpers.get_from_dict(keys, _loaded)
    return value or default


def get_device():
    import app.devices
    return app.devices.load_device(get('device.name'), get('device.type', 'mouse'))


# App config
debug = get('app.debug', False)
force = get('app.force', False)
json_indent = get('app.json_indent', 4)
