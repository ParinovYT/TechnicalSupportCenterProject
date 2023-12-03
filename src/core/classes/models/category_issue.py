from src.core.classes.models import BaseModel


class ModelTemplateIssue(BaseModel):
    def __init__(self):
        super().__init__()
        self.__id: int
        self.__value: str
    
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int):
        self.__id = value

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value
