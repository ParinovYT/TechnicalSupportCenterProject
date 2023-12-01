from abc import ABC, abstractmethod


class HashBase(ABC):
    @abstractmethod
    def sha(self): ...

    @abstractmethod
    def _sha256(self): ...
