from src.core.classes.template_issue.base import TemplateIssueBase
from src.core.template_issue import TemplateIssueGet

class TemplateIssue:
    def get(self):
        obj: TemplateIssueBase = TemplateIssueGet()
        return obj