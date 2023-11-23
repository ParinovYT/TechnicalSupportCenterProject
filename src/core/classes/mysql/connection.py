from abc import ABC, abstractmethod

class MySqlConnection(ABC):
    @abstractmethod
    def open():...

    @abstractmethod
    def close():...