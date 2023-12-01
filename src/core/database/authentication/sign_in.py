from http.client import CONFLICT, INTERNAL_SERVER_ERROR, OK

from mysql.connector.errors import InterfaceError

from src.core.classes.models.token import ModelToken
from src.core.classes.mysql.queries import MySqlQuery
from src.core.database.connection import Connection


class SignIn(MySqlQuery):
    def __init__(self, connection: Connection, model_token: ModelToken):
        super().__init__(connection)
        self.__model_token: ModelToken = model_token

    @property
    def status_code(self) -> int:
        return self._status_code

    def execute(self) -> None:
        try:
            cursor = self._connection.connection.cursor(prepared=True, )
            insert_query = """
            INSERT INTO tokens VALUE (NULL, %s, %s, %s, %s, %s)
            """

            params = (
                self.__model_token.user_id,
                self.__model_token.token,
                self.__model_token.created_at,
                self.__model_token.updated_at,
                self.__model_token.expiration,
            )
            cursor.execute(insert_query, params)
            self._connection.connection.commit()

            self._status_code = OK

        except InterfaceError:
            self._status_code = CONFLICT

        except Exception:
            self._status_code = INTERNAL_SERVER_ERROR
