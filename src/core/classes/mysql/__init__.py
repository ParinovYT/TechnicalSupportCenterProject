from src.core.database.authentication import Authentication
from src.core.classes.mysql.queries import MySqlQuery
from src.core.classes.mysql.connection import MySqlConnection
from src.core.database.connection import Connection


class MySql:
    def connection(self):
        connection: MySqlConnection = Connection()
        return connection

    def queries(self):
        return MySqlQuery