class ModelUser:
    def __init__(self):
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
        self.__username = value
    
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value: str):
        self.__password = value

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, value: int):
        self.__created_at = value
    
    @property
    def rule(self):
        return self.__rule

    @rule.setter
    def rule(self, value: int):
        self.__rule = value

    @property
    def admin(self):
        return self.__admin

    @admin.setter
    def admin(self, value: bool):
        self.__admin = value