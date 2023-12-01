from src.core.classes.security.hash import HashBase
from src.core.security.hash import Hash


class Security:
    def hash(self) -> Hash:
        obj: HashBase = Hash()
        return obj
