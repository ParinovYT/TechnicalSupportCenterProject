from src.core.classes.models import BaseModel


class ModelDevice(BaseModel):
    def __init__(self):
        super().__init__()
        self.__id: int
        self.__inventory_number: str
        self.__object_name: str
        self.__year_issue: str
        self.__floor: int
        self.__office_number: str

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int):
        self.__id = value

    @property
    def inventory_number(self) -> str:
        return self.__inventory_number

    @inventory_number.setter
    def inventory_number(self, value: str):
        self.__inventory_number = value

    @property
    def object_name(self) -> str:
        return self.__object_name

    @object_name.setter
    def object_name(self, value: str):
        self.__object_name = value

    @property
    def year_issue(self) -> str:
        return self.__year_issue

    @year_issue.setter
    def year_issue(self, value: str):
        self.__year_issue = value

    @property
    def floor(self) -> int:
        return self.__floor

    @floor.setter
    def floor(self, value: int):
        self.__floor = value

    @property
    def office_number(self) -> str:
        return self.__office_number

    @office_number.setter
    def office_number(self, value: str):
        self.__office_number = value
