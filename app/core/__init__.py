import app.config
from app.core.device_handler import DeviceHandler


def _print(*args, **kwargs):
    print(*args, **kwargs)


def debug(*args, **kwargs):
    if app.config.debug:
        _print('[DEBUG]: ', *args, **kwargs)


def info(*args, **kwargs):
    if not app.config.quiet:
        _print(*args, **kwargs)


def verbose(*args, **kwargs):
    if app.config.verbose or app.config.debug:
        _print(*args, **kwargs)
