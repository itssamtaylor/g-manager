import app.config


def read_from_device():
    from app.readers import DeviceReader
    return DeviceReader(app.config.get_device()).get_reports()


def read_from_file():
    from app.readers import FileReader
    return FileReader(app.config.source).get_reports()


def write_to_device(report_list):
    from app.writers import DeviceWriter
    DeviceWriter(app.config.get_device()).write_reports(report_list)


def write_to_file(report_list):
    from app.writers import FileWriter
    FileWriter(app.config.destination).write_reports(report_list)


def write_to_stdout(report_list):
    print(report_list)


def run():
    if app.config.source == app.config.device_accessor:
        report_list = read_from_device()
    else:
        report_list = read_from_file()

    if app.config.destination == app.config.device_accessor:
        write_to_device(report_list)
    elif app.config.destination is None:
        write_to_stdout(report_list)
    else:
        write_to_file(report_list)
