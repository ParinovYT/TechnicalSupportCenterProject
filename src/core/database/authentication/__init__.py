from src.core.database.connection import Connection
from src.core.classes.models.user import ModelUser
from src.core.classes.mysql.queries import MySqlQuery
from src.core.database.authentication.sign_up import SignUp


class Authentication:
    def __init__(self, connection: Connection):
        self.__connection: Connection = connection

    def sign_up(self, model: ModelUser):
        obj: MySqlQuery = SignUp(self.__connection, model)
        return obj
    
    def sign_in(self, model: ModelUser):...