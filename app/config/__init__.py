from app.config.argument_loader import ArgumentLoader
from app.config.file_loader import FileLoader

_arguments = ArgumentLoader().get_loaded()
_file = FileLoader(_arguments['config_file']).get_loaded()
_device = None


def get(key, default=None):
    import app.helpers
    arg_value = app.helpers.get_from_dict(key, _arguments)
    file_value = app.helpers.get_from_dict(key, _file)
    return arg_value or file_value or default


def _load_device():
    import app.devices
    global _device
    if _arguments['device'] is not None:
        *device_type, device_name = _arguments['device'].split('.')
        _device = app.devices.load_device(device_name, '.'.join(device_type))
    else:
        _device = app.devices.load_device(_file['device']['name'], _file['device']['type'])


def get_device():
    if _device is None:
        _load_device()
    return _device


device_accessor: str = 'DEVICE'

source: str = _arguments['source']
destination: str | None = _arguments['destination']
as_bytes: bool = _file['app']['as_bytes'] | _arguments['as_bytes']
force: bool = _file['app']['force'] | _arguments['force']
dry_run: bool = _file['app']['dry_run'] | _arguments['dry_run']
debug: bool = _file['app']['debug'] | _arguments['debug']
verbose: bool = _file['app']['verbose'] | _arguments['verbose']
quiet: bool = _file['app']['quiet'] | _arguments['quiet']
json_indent: int = _file['app']['json_indent']
