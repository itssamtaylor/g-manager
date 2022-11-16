import app.config


def read_from_device():
    from app.readers import DeviceReader
    return DeviceReader(app.config.get_device()).get_reports()


def read_from_file():
    return {}


def write_to_device(data):
    pass


def write_to_file(data):
    pass


def write_to_stdout(data):
    if isinstance(data, list):
        for d in data:
            print(d)
    else:
        print(data)


def run():
    if app.config.source == app.config.device_accessor:
        data = read_from_device()
    else:
        data = read_from_file()

    if app.config.destination == app.config.device_accessor:
        write_to_device(data)
    elif app.config.destination is None:
        write_to_stdout(data)
    else:
        write_to_stdout(data)
