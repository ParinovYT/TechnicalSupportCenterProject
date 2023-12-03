from abc import ABC, abstractmethod

from src.core.classes.mysql import MySqlBase


class TemplateIssueBase(ABC):
    def __init__(self):
        self._status_code: int = 0
        self._response: str = ''
        self._DB = MySqlBase()

    @abstractmethod
    def execute(self) -> None:...