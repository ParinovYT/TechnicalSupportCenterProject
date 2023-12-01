from src.core.classes.security import Security


class BaseModel:
    def __init__(self):
        self._hash = Security().hash()
