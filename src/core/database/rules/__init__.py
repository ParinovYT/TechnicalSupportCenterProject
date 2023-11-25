from http.client import INTERNAL_SERVER_ERROR, OK
from src.core.database.connection import Connection
from src.core.classes.mysql.queries import MySqlQuery

class Rules(MySqlQuery):
    def __init__(self, connection: Connection):
        super().__init__(connection)

    @property
    def get(self) -> int:
        """Returns the role id"""
        return self._response

    @property
    def status_code(self) -> int:
        return self._status_code

    def execute(self, value: str) -> None:
        try:
            cursor = self._connection.connection.cursor()

            cursor.execute("SELECT id FROM rules WHERE name=%s", (value,))

            row = cursor.fetchone()

            if row:
                self._response = int(row[0])
                self._status_code = OK
            else:
                self._response = -1
                self._status_code = INTERNAL_SERVER_ERROR

        except Exception as e:
            self._response = -1
            self._status_code = INTERNAL_SERVER_ERROR
            print(e)