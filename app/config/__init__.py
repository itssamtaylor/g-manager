from app.config.argument_loader import ArgumentLoader
from app.config.file_loader import FileLoader

_arguments = ArgumentLoader().get_loaded()
_file = FileLoader(_arguments['config_file']).get_loaded()
_device = None


def get(key, default=None, file_parent_key=None):
    import app.helpers
    arg_value = app.helpers.get_from_dict(key, _arguments)
    file_value = app.helpers.get_from_dict(key, _file if file_parent_key is None else _file[file_parent_key])
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


source: str = get('source')
destination: str | None = get('destination', None)
as_bytes: bool = get('as_bytes', file_parent_key='app')
minified: bool = get('minified', file_parent_key='app')
overwrite: bool = get('overwrite', file_parent_key='app')
dry_run: bool = get('dry_run', file_parent_key='app')
debug: bool = get('debug', file_parent_key='app')
verbose: bool = get('verbose', file_parent_key='app')
quiet: bool = get('quiet', file_parent_key='app')
force: bool = get('force', file_parent_key='app')
lenient: bool = get('lenient', file_parent_key='app')
json_indent: int | None = get('app.json_indent', 4) if not minified else None
device_accessor: str = get('app.device_accessor', 'DEVICE')
