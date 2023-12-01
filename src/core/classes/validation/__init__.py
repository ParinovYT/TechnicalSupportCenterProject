from abc import ABC, abstractmethod


class ValidationBase(ABC):
    @abstractmethod
    def is_username(self, value: str) -> bool: ...

    @abstractmethod
    def is_password(self, value: str) -> bool: ...
