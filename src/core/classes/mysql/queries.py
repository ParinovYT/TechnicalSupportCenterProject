from abc import ABC, abstractmethod

class MySqlQuery(ABC):
    @abstractmethod
    def execute() -> None:...