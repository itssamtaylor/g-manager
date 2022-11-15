import app.devices
from app.fields.byte import ByteField


def multi_print(data, indent: str = ''):
    if isinstance(data, object) and hasattr(data, '_instance_map'):
        multi_print(data._instance_map, indent + '  ')
    elif isinstance(data, list):
        for item in data:
            multi_print(item, indent + '  ')
    elif isinstance(data, tuple):
        value = indent + '"' + str(data[0]) + '": '
        if isinstance(data[1], ByteField):
            value += '"' + str(data[1]._readable_value) + '"'
            print(value)
        else:
            value += '{'
            print(value)
            multi_print(data[1], indent + '  ')
            print(indent + '}')


class Transformer:
    device: app.devices.Device = None

    modes = []

    def __init__(self, device: app.devices.Device):
        self.device = device

    def p(self):
        multi_print(self.modes)

    def t(self):
        for i in range(len(self.device.report_ids)):
            self.modes.append(
                ('mode' + str(i + 1), self.buildMode())
            )

    def buildMode(self):
        mode = []
        for i in self.device.map_report_to():
            mode.append((i.__class__.__name__, i))
        return mode
