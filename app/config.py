import toml
import devices

_loaded = toml.load('config.toml')


def _load_device() -> devices.Device:
    name = _loaded['device']['name']
    module = __import__('devices.' + _loaded['device']['type'] + '.' + name, globals(), locals(), [name])
    class_name = getattr(module, name)
    return class_name()


# App config
debug = _loaded['app']['debug']
force = _loaded['app']['force']
json_indent = _loaded['app']['json_indent']

# Device config
device = _load_device()

vendor_id = device.vendor_id if not None else _loaded['device_defaults']['vendor_id']

# HID config
hid_read_type = device.hid_read_type if not None else _loaded['hid_defaults']['hid_read_type']
hid_read_request = device.hid_read_request if not None else _loaded['hid_defaults']['hid_read_request']
hid_read_index = device.hid_read_index
hid_write_type = device.hid_write_type if not None else _loaded['hid_defaults']['hid_write_type']
hid_write_request = device.hid_write_request if not None else _loaded['hid_defaults']['hid_write_request']
hid_write_index = device.hid_write_index
hid_timeout = device.hid_timeout if not None else _loaded['hid_defaults']['hid_timeout']