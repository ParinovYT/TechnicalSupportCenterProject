from abc import abstractmethod

from src.core.classes.mysql.connection import MySqlConnection
from src.core.database.connection import Connection


class MySql:
    def connection(self):
        connection: MySqlConnection = Connection()
        return connection

    @abstractmethod
    def queries():...