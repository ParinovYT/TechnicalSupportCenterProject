from src.core.user.authentication import UserAuthentication
from src.core.classes.authentication import AuthenticationBase


class User:
    def sign_up(self):
        obj: AuthenticationBase = UserAuthentication()
        return obj