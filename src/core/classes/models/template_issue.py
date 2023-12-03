from src.core.classes.models import BaseModel


class ModelTemplateIssue(BaseModel):
    def __init__(self):
        super().__init__()
        self.__id: int
        self.__category_id: int
        self.__issue: str
        self.__solution: str
    
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int):
        self.__id = value

    @property
    def category_id(self) -> int:
        return self.__category_id

    @category_id.setter
    def category_id(self, value: int):
        self.__category_id = value

    @property
    def issue(self) -> str:
        return self.__issue

    @issue.setter
    def issue(self, value: str):
        self.__issue = value

    @property
    def solution(self) -> str:
        return self.__solution

    @solution.setter
    def solution(self, value: str):
        self.__solution = value
