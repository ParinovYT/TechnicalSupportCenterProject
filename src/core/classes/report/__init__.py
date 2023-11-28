from src.core.report import Create
from src.core.classes.report.base import ReportBase


class Report:
    def create(self):
        obj: ReportBase = Create()
        return obj

    def get(self):...

    def change(self):...

    def delete(self):...