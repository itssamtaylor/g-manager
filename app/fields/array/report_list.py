from app.fields.array import ArrayField
from app.fields.composite import Report


class ReportList(ArrayField):
    _field_type = Report
