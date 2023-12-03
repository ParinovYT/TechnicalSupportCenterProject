from http.client import OK
import json

from src.core.classes.template_issue import TemplateIssue

def test_template_issue():
    __obj = TemplateIssue()
    obj = __obj.get()
    obj.execute()

    assert obj.status_code == OK, obj.status_code