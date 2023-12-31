from abc import ABC, abstractmethod

from src.core.classes.models.device import ModelDevice
from src.core.classes.models.issue import ModelIssue
from src.core.classes.models.token import ModelToken
from src.core.classes.mysql import MySqlBase


class ReportBase(ABC):
    def __init__(self) -> None:
        self._status_code: int
        self._DB = MySqlBase()
        self._model_issue = ModelIssue()
        self._model_token = ModelToken()
        self._model_device = ModelDevice()

    @abstractmethod
    def execute(self) -> None: ...
