from app.fields.byte import ByteField


class ReportID(ByteField):
    def make_readable_value(self, byte):
        for report_id in self.device.report_ids:
            if self.make_byte_value(report_id) == byte:
                return report_id
        return None

    def make_byte_value(self, readable):
        return int(readable) & 0xff
