from src.core.user.authentication.sign_in import SignIn
from src.core.user.authentication import SignUp
from src.core.classes.authentication import AuthenticationBase

class User:
    def __init__(self, admin: bool = False) -> None:
        self._admin: bool = admin

    def sign_up(self) -> SignUp:
        obj: AuthenticationBase = SignUp(self._admin)
        return obj
    
    def sign_in(self) -> SignIn:
        obj: AuthenticationBase = SignIn(self._admin)
        return obj

"""
class Admin(User):
    def __init__(self) -> None:
        super().__init__(True)

    def sign_up(self) -> SignUp:
        return super().sign_up()
"""