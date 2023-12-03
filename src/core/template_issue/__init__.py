from http.client import INTERNAL_SERVER_ERROR
from src.core.classes.template_issue.base import TemplateIssueBase
from src.core.database.template_issue import TemplateIssue

from mysqlx import Error

class TemplateIssueGet(TemplateIssueBase):
    def __init__(self):
        super().__init__()
    
    @property
    def status_code(self) -> int:
        return self._status_code
    
    @property
    def response(self) -> str:
        return self._response

    def execute(self) -> None:
        MySQl = self._DB
        db_connection = MySQl.connection()
        MySQlQueries = MySQl.queries()
        query: MySQlQueries = TemplateIssue(db_connection)
        try:
            db_connection.open()
            query.execute()
            self._status_code = query.status_code
            self._response = query.get
            return

        except Error as e:
            print(e)
            self._status_code = INTERNAL_SERVER_ERROR

        finally:
            db_connection.close()