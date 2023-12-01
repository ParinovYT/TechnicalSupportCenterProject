import secrets
import string
import time
from http.client import BAD_REQUEST, INTERNAL_SERVER_ERROR, OK

from mysql.connector.errors import Error

from src.core.classes.authentication import AuthenticationBase
from src.core.database.authentication import Authentication
from src.core.database.user_info import UserInfo


class SignIn(AuthenticationBase):

    def __init__(self, admin: bool = False):
        super().__init__(admin=admin)
        self.__token: str = ""

    @property
    def status_code(self) -> int:
        return self._status_code

    @property
    def get_token(self) -> str:
        return self.__token

    def __generate_token(self, length: int) -> str:
        return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))

    def execute(self, username: str, password: str, expiration: int):
        MySQl = self._DB
        db_connection = MySQl.connection()

        try:
            db_connection.open()
            MySQlQueries = MySQl.queries()
            query_user_info: MySQlQueries = UserInfo(db_connection)

            self._user_model.username = username
            self._user_model.password = password

            query_user_info.execute(self._user_model.username, self._user_model.password)

            if query_user_info.status_code != OK:
                self._status_code = query_user_info.status_code
                return

            token = self.__generate_token(256)
            self.__token = token

            self._token_model.user_id = query_user_info.id
            self._token_model.token = token
            self._token_model.created_at = int(time.time())
            self._token_model.updated_at = int(time.time())
            self._token_model.expiration = expiration

            query_sign_in: MySQlQueries = Authentication(db_connection).sign_in(self._token_model)
            query_sign_in.execute()
            self._status_code = query_sign_in.status_code
            return

        except ValueError:
            self._status_code = BAD_REQUEST

        except Error as e:
            print(e)
            self._status_code = INTERNAL_SERVER_ERROR

        finally:
            db_connection.close()
