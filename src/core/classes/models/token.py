from src.core.classes.models import BaseModel


class ModelToken(BaseModel):
    def __init__(self):
        super().__init__()
        self.__user_id: int
        self.__token: str
        self.__created_at: int
        self.__updated_at: int
        self.__expiration: int
    
    @property
    def user_id(self) -> int:
        return self.__user_id

    @user_id.setter
    def user_id(self, value: int):
        self.__user_id = value

    @property
    def token(self) -> str:
        return self.__token

    @token.setter
    def token(self, value: str):
        if len(value) == 256:
            self.__token = str(self._hash.sha(value))
            return
        raise ValueError(f'Invalid token value, length = {len(value)}')

    @property
    def created_at(self) -> int:
        return self.__created_at

    @created_at.setter
    def created_at(self, value: int):
        self.__created_at = value

    @property
    def updated_at(self) -> int:
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, value: int):
        self.__updated_at = value

    @property
    def expiration(self) -> int:
        return self.__expiration

    @expiration.setter
    def expiration(self, value: int):
        self.__expiration = value