import app.config


def read_from_device(device):
    from app.readers import DeviceReader
    return DeviceReader(device).get_reports()


def read_from_file(file):
    from app.readers import FileReader
    return FileReader(file).get_reports()


def write_to_device(report_list, device):
    from app.writers import DeviceWriter
    DeviceWriter(device).write_reports(report_list)


def write_to_file(report_list, destination):
    from app.writers import FileWriter
    FileWriter(destination).write_reports(report_list)


def write_to_stdout(report_list):
    if app.config.as_bytes:
        print(report_list.bytes_to_json(indent=2))
    else:
        print(report_list.to_json(indent=2))


def run():
    if app.config.source == app.config.device_accessor:
        report_list = read_from_device(app.config.get_device())
    else:
        report_list = read_from_file(app.config.source)

    if app.config.destination == app.config.device_accessor:
        write_to_device(report_list, app.config.get_device())
    elif app.config.destination is None:
        write_to_stdout(report_list)
    else:
        write_to_file(report_list, app.config.destination)
