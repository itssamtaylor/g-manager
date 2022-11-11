class Device:
    vendor_id = None
    product_id = None
    control_interface = None
    report_ids = ()
    unknown_group_indexes = []
    read_length = None
    hid_read_type = None
    hid_read_request = None
    hid_read_index = None
    hid_write_type = None
    hid_write_request = None
    hid_write_index = None
    hid_timeout = None

    def __init__(self):
        self.num_unknown_groups = len(self.unknown_group_indexes)
        self.num_reports = len(self.report_ids)

        if self.hid_read_index is None:
            self.hid_read_index = self.control_interface

        if self.hid_write_index is None:
            self.hid_write_index = self.control_interface

