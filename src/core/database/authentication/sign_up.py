from http.client import CONFLICT, INTERNAL_SERVER_ERROR, OK
from mysql.connector.errors import InterfaceError

from src.core.classes.models.user import ModelUser
from src.core.classes.mysql.queries import MySqlQuery
from src.core.database.connection import Connection


class SignUp(MySqlQuery):
    def __init__(self, connection: Connection, model: ModelUser):
        self.__status_code: int
        self.__model: ModelUser = model
        self.__connection: Connection = connection
    
    @property
    def status_code(self) -> int:
        return self.__status_code
    
    def execute(self) -> None:
        try:
            cursor = self.__connection.connection.cursor(prepared=True,)
            insert_query = "INSERT INTO users VALUES (NULL, %s, %s, %s, %s, %s);"
            params = (
                self.__model.username,
                self.__model.password,
                self.__model.created_at,
                self.__model.rule,
                self.__model.admin
            )
            cursor.execute(insert_query, params)
            self.__connection.connection.commit()

            self.__status_code = OK

        except InterfaceError:
            self.__status_code = CONFLICT
        