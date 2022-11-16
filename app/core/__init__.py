import app.config
from app.core.device_handler import DeviceHandler


def _print(*args):
    print(*args)


def debug(*args):
    if app.config.debug:
        _print(*args)


def info(*args):
    if not app.config.quiet:
        _print(*args)


def verbose(*args):
    if app.config.verbose or app.config.debug:
        _print(*args)
