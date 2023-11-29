from abc import ABC, abstractmethod
from src.core.classes.models.token import ModelToken
from src.core.classes.mysql import MySqlBase
from src.core.classes.models.user import ModelUser
from src.core.database.rules import Rules

class AuthenticationBase(ABC):
    def __init__(self, admin: bool = False):
        self._status_code: int = 0
        self._DB = MySqlBase()
        self._user_model = ModelUser()
        self._token_model = ModelToken()
        self._admin: bool = admin

    @abstractmethod
    def execute(self) -> None:
        pass

    def _get_rule_by_name(self, value: str) -> int:
        MySQl = self._DB
        db_connection = MySQl.connection()
        try:
            db_connection.open()
            MySQlQueries = MySQl.queries()

            rules_query: MySQlQueries = Rules(db_connection)
            rules_query.execute(value)

            return rules_query.get
        
        except Exception:
            return -1

        finally:
            db_connection.close()