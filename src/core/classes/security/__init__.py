from src.core.security.hash import Hash
from src.core.classes.security.hash import HashBase

class Security:
    def hash(self) -> Hash:
        obj: HashBase = Hash()
        return obj