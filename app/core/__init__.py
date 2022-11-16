import app.config
from app.core.device_handler import DeviceHandler


def _print(prefix=None, show_prefix=True, *args, **kwargs):
    if prefix is None or not show_prefix:
        print(*args, **kwargs)
    else:
        print('[{}]: '.format(prefix), *args, **kwargs)


def debug(*args, prefix=True, **kwargs):
    if app.config.debug:
        _print('DEBUG', prefix, *args, **kwargs)


def info(*args, prefix=True, **kwargs):
    if not app.config.quiet:
        _print('INFO', prefix, *args, **kwargs)


def warning(*args, prefix=True, **kwargs):
    if not app.config.quiet:
        _print('WARNING', prefix, *args, **kwargs)


def verbose(*args, prefix=True, **kwargs):
    if app.config.verbose or app.config.debug:
        _print('DETAIL', prefix, *args, **kwargs)
