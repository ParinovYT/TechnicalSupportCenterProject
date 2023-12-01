from http.client import INTERNAL_SERVER_ERROR, NOT_FOUND, OK

from mysql.connector.errors import InterfaceError

from src.core.classes.models.token import ModelToken
from src.core.classes.mysql.queries import MySqlQuery
from src.core.database.connection import Connection


class SignOut(MySqlQuery):
    def __init__(self, connection: Connection, model: ModelToken):
        super().__init__(connection)
        self.__model_token: ModelToken = model

    @property
    def status_code(self) -> int:
        return self._status_code

    def execute(self) -> None:
        try:
            cursor = self._connection.connection.cursor(prepared=True, )
            query = """
            DELETE FROM tokens WHERE user_id = %s AND token = %s
            """

            params = (
                self.__model_token.user_id,
                self.__model_token.token
            )

            cursor.execute(query, params)
            self._connection.connection.commit()

            self._status_code = OK

        except InterfaceError:
            self._status_code = NOT_FOUND

        except Exception:
            self._status_code = INTERNAL_SERVER_ERROR
