from app.devices.device import Device


def load_device(name: str, device_type: str = 'mouse') -> Device:
    module = __import__('app.devices.' + device_type + '.' + name, globals(), locals(), [name])
    class_name = getattr(module, name)
    return class_name()
