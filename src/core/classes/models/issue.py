from typing import Literal

from src.core.classes.models import BaseModel


class ModelIssue(BaseModel):
    def __init__(self):
        super().__init__()
        self.__id: int
        self.__user_id: int
        self.__issue: str
        self.__comments: str
        self.__device_id: int
        self.__created_at: int
        self.__updated_at: int
        self.__line: int
        self.__status: bool

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int):
        self.__id = value

    @property
    def user_id(self) -> int:
        return self.__user_id

    @user_id.setter
    def user_id(self, value: int):
        self.__user_id = value

    @property
    def issue(self) -> str:
        return self.__issue

    @issue.setter
    def issue(self, value: str):
        value_len: int = 256
        if len(value) > value_len:
            raise ValueError(f'Max issue length {value_len}')
        self.__issue = value

    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, value: str):
        value_len: int = 1024
        if len(value) > value_len:
            raise ValueError(f'Max comments length {value_len}')
        self.__comments = value

    @property
    def device_id(self) -> int:
        return self.__device_id

    @device_id.setter
    def device_id(self, value: int):
        self.__device_id = value

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
    def line(self) -> int:
        return self.__line

    @line.setter
    def line(self, value: Literal[1, 2, 3]):
        self.__line = value

    @property
    def status(self) -> bool:
        return self.__status

    @status.setter
    def status(self, value: bool):
        self.__status = value
