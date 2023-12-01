from src.core.classes.mysql.connection import MySqlConnection
from src.core.classes.mysql.queries import MySqlQuery
from src.core.database.connection import Connection


class MySqlBase:
    def connection(self):
        connection: MySqlConnection = Connection()
        return connection

    def queries(self):
        return MySqlQuery
