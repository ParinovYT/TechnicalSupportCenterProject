from http.client import INTERNAL_SERVER_ERROR, UNAUTHORIZED, OK

from mysqlx import InterfaceError

from src.core.classes.models.issue import ModelIssue
from src.core.classes.mysql.queries import MySqlQuery
from src.core.database.connection import Connection


class Create(MySqlQuery):
    def __init__(self, connection: Connection, model_issue: ModelIssue) -> None:
        super().__init__(connection)
        self.__model_issue: ModelIssue = model_issue

    @property
    def status_code(self) -> int:
        return self._status_code

    def execute(self) -> None:
        try:
            cursor = self._connection.connection.cursor(prepared=True, )
            insert_query = """
            INSERT INTO issues VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            params = (
                self.__model_issue.user_id,
                self.__model_issue.issue,
                self.__model_issue.comments,
                self.__model_issue.device_id,
                self.__model_issue.created_at,
                self.__model_issue.updated_at,
                self.__model_issue.line,
                self.__model_issue.status,
                self.__model_issue.worker
            )

            cursor.execute(insert_query, params)
            self._connection.connection.commit()

            self._status_code = OK

        except InterfaceError:
            self._status_code = UNAUTHORIZED

        except Exception:
            self._status_code = INTERNAL_SERVER_ERROR
        return
