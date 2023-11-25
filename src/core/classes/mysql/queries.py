from abc import ABC, abstractmethod
from typing import Any

from src.core.database.connection import Connection

class MySqlQuery(ABC):
    def __init__(self, connection: Connection):
        self._connection: Connection = connection
        self._status_code: int
        self._response: Any

    @abstractmethod
    def execute(self) -> None:...