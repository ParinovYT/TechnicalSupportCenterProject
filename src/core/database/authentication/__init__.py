from src.core.classes.models.token import ModelToken
from src.core.classes.models.user import ModelUser
from src.core.classes.mysql.queries import MySqlQuery
from src.core.database.authentication.sign_in import SignIn
from src.core.database.authentication.sign_out import SignOut
from src.core.database.authentication.sign_up import SignUp
from src.core.database.connection import Connection


class Authentication:
    def __init__(self, connection: Connection):
        self.__connection: Connection = connection

    def sign_up(self, model: ModelUser):
        obj: MySqlQuery = SignUp(self.__connection, model)
        return obj

    def sign_in(self, model_token: ModelToken):
        obj: MySqlQuery = SignIn(self.__connection, model_token)
        return obj

    def sign_out(self, model_token: ModelToken):
        obj: MySqlQuery = SignOut(self.__connection, model_token)
        return obj
