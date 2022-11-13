import app.devices


def multi_print(data, indent: str = ''):
    if isinstance(data, object) and hasattr(data, 'test_data'):
        multi_print(data.test_data(), indent + '  ')
    elif isinstance(data, list):
        for item in data:
            multi_print(item, indent + '  ')
    elif isinstance(data, tuple):
        print(indent + '"' + str(data[0]) + '": {')
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
