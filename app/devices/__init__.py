import app.config


class Device:
    vendor_id: int = app.config.get('device_defaults.vendor_id')
    product_id: int = None
    control_interface: int = None
    report_ids: tuple[int] = ()
    unknown_group_indexes: list[tuple[int]] = []
    read_length: int = None
    hid_read_type: int = app.config.get('hid_defaults.hid_read_type')
    hid_read_request: int = app.config.get('hid_defaults.hid_read_request')
    hid_read_index: int = None
    hid_write_type: int = app.config.get('hid_defaults.hid_write_type')
    hid_write_request: int = app.config.get('hid_defaults.hid_write_request')
    hid_write_index: int = None
    hid_timeout: int = app.config.get('hid_defaults.hid_timeout')

    def __init__(self):
        self.num_unknown_groups = len(self.unknown_group_indexes)
        self.num_reports = len(self.report_ids)

        if self.hid_read_index is None:
            self.hid_read_index = self.control_interface

        if self.hid_write_index is None:
            self.hid_write_index = self.control_interface

    def map_report_to(self):
        raise NotImplemented


def load_device(name: str, device_type: str = 'mouse') -> Device:
    module = __import__('app.devices.' + device_type + '.' + name, globals(), locals(), [name])
    class_name = getattr(module, name)
    return class_name()
