
from src.core.classes.models import BaseModel
from src.core.validation import Validation
from src.core.classes.validation import ValidationBase


class ModelUser(BaseModel):
    def __init__(self):
        super().__init__()
        self.__validation: ValidationBase = Validation()
        self.__username: str
        self.__password: str
        self.__created_at: int
        self.__rule: int
        self.__admin: bool

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, value: str):
        if self.__validation.is_username(value):
            self.__username = value
            return
        raise ValueError('Can only be present: hyphen, underscore, Latin characters only')
    
    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, value: str):
        if self.__validation.is_password(value):
            self.__password = str(self._hash.sha(value))
            return
        raise ValueError('Password does not meet the minimum requirements: one upper case character, one lower case character, one digit, one special character, length from 8 to 64 characters.')

    @property
    def created_at(self) -> int:
        return self.__created_at

    @created_at.setter
    def created_at(self, value: int):
        self.__created_at = value
    
    @property
    def rule(self) -> int:
        return self.__rule

    @rule.setter
    def rule(self, value: int):
        self.__rule = value

    @property
    def admin(self) -> bool:
        return self.__admin

    @admin.setter
    def admin(self, value: bool):
        self.__admin = value