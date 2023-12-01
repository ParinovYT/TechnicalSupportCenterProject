from http.client import BAD_REQUEST, OK

from src.core.classes.authentication import AuthenticationBase
from src.core.database.authentication import Authentication
from src.core.database.user_info import UserInfo


class SignOut(AuthenticationBase):

    def __init__(self, admin: bool = False):
        super().__init__(admin=admin)

    @property
    def status_code(self) -> int:
        return self._status_code

    def execute(self, token: str):
        MySQl = self._DB
        db_connection = MySQl.connection()
        MySQlQueries = MySQl.queries()
        query_user_info: MySQlQueries = UserInfo(db_connection)

        try:
            db_connection.open()
            self._token_model.token = token
            query_user_info.execute(token=self._token_model.token)

            if query_user_info.status_code != OK:
                self._status_code = query_user_info.status_code
                return

            self._token_model.user_id = query_user_info.id

            MySQlQueries = MySQl.queries()
            query: MySQlQueries = Authentication(db_connection).sign_out(self._token_model)
            query.execute()
            self._status_code = query.status_code
            return

        except ValueError:
            self._status_code = BAD_REQUEST

        finally:
            db_connection.close()
