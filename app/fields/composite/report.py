from app.fields.composite import CompositeField


class Report(CompositeField):
    composition_map = []

    def init(self):
        self.composition_map = self.device.get_report_map()
