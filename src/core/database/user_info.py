from http.client import INTERNAL_SERVER_ERROR, OK

from mysql.connector.errors import Error 
from src.core.database.connection import Connection
from src.core.classes.mysql.queries import MySqlQuery


class UserInfo(MySqlQuery):
    def __init__(self, connection: Connection):
        super().__init__(connection)
        self.__id: int
        self.__username: str
        self.__created_at: int
        self.__rule: int
        self.__admin: bool

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def username(self) -> str:
        return self.__username

    @property
    def created_at(self) -> int:
        return self.__created_at

    @property
    def rule(self) -> int:
        return self.__rule

    @property
    def admin(self) -> bool:
        return self.__admin

    @property
    def status_code(self) -> int:
        return self._status_code

    def execute(self, username: str, password: str) -> None:
        try:
            cursor = self._connection.connection.cursor()

            cursor.execute("""
            SELECT id, username, created_at, rule, admin FROM users
            WHERE username = %s AND password = %s
            """, (username, password))

            row = cursor.fetchone()

            if row:
                self.__id = int(row[0])
                self.__username = str(row[1])
                self.__created_at = int(row[2])
                self.__rule = int(row[3])
                self.__admin = bool(row[4])
                self._status_code = OK
            else:
                self._status_code = INTERNAL_SERVER_ERROR

        except Error as e:
            self._status_code = INTERNAL_SERVER_ERROR
            print(e)