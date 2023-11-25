from abc import ABC, abstractmethod
from src.core.classes.mysql import MySqlBase
from src.core.classes.models.user import ModelUser
from src.core.database.rules import Rules

class AuthenticationBase(ABC):
    def __init__(self):
        self._status_code: int
        self._DB: MySqlBase  # You need to initialize this in the subclasses
        self._user_model = ModelUser()

    @abstractmethod
    def execute(self) -> None: ...

    def _get_rule_by_name(self, value: str) -> int:
        MySQl = self._DB  # Fix typo: MySQl instead of MySql
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