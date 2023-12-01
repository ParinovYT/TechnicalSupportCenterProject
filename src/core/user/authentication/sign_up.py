import time
from http.client import BAD_REQUEST

from src.core.classes.authentication import AuthenticationBase
from src.core.database.authentication import Authentication
from src.core.database.rules.consts import USER


class SignUp(AuthenticationBase):

    def __init__(self, admin: bool = False):
        super().__init__(admin=admin)  # Call the superclass constructor

    @property
    def status_code(self) -> int:
        return self._status_code

    def execute(self, username: str, password: str):
        MySQl = self._DB
        db_connection = MySQl.connection()

        try:
            self._user_model.username = username
            self._user_model.password = password
            self._user_model.created_at = int(time.time())
            self._user_model.rule = self._get_rule_by_name(USER)
            self._user_model.admin = self._admin

            db_connection.open()
            MySQlQueries = MySQl.queries()
            query: MySQlQueries = Authentication(db_connection).sign_up(self._user_model)
            query.execute()
            self._status_code = query.status_code
            return

        except ValueError:
            self._status_code = BAD_REQUEST

        finally:
            db_connection.close()
