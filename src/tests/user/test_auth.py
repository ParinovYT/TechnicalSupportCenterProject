from http.client import BAD_REQUEST, CONFLICT, OK

from src.core.classes.user import User

USERNAME = 'user23_---'
PASSWORD = ')O#$VJ)#@MCO#NJKV43nkjc32v'
EXPIRATION = 600


class SignUp:
    def __init__(self) -> None:
        self.__ok: int
        self.__bad_request: int
        self.__conflict: int

    @property
    def ok(self) -> int:
        return self.__ok

    @property
    def bad_request(self) -> int:
        return self.__bad_request

    @property
    def conflict(self) -> int:
        return self.__conflict

    def exec(self):
        user_obj = User().sign_up()
        user_obj.execute(USERNAME, PASSWORD)
        self.__ok = user_obj.status_code

        user_obj.execute('1', '43432v42c3')
        self.__bad_request = user_obj.status_code

        user_obj.execute(USERNAME, PASSWORD)
        self.__conflict = user_obj.status_code


class SignIn:
    def __init__(self) -> None:
        self.__ok: int
        self.__bad_request: int
        self.__token: str

    @property
    def ok(self) -> int:
        return self.__ok

    @property
    def token(self) -> str:
        return self.__token

    @property
    def bad_request(self) -> int:
        return self.__bad_request

    def exec(self):
        user_obj = User().sign_in()
        user_obj.execute(USERNAME, PASSWORD, EXPIRATION)
        self.__ok = user_obj.status_code
        self.__token = user_obj.get_token

        user_obj.execute('1', '43432v42c3', EXPIRATION)
        self.__bad_request = user_obj.status_code


class SignOut:
    def __init__(self, token: str) -> None:
        self.__ok = 0  # Set an initial value
        self.__bad_request = 0  # Set an initial value
        self.__token = token

    @property
    def ok(self) -> int:
        return self.__ok

    @property
    def bad_request(self) -> int:
        return self.__bad_request

    def exec(self):
        user_obj = User().sign_out()
        user_obj.execute(self.__token)
        self.__ok = user_obj.status_code

        user_obj.execute('v23c423v3')
        self.__bad_request = user_obj.status_code


def test():
    sign_up = SignUp()
    sign_up.exec()

    assert sign_up.ok == OK, sign_up.ok
    assert sign_up.bad_request == BAD_REQUEST, sign_up.bad_request
    assert sign_up.conflict == CONFLICT, sign_up.conflict

    sign_in = SignIn()
    sign_in.exec()

    assert sign_in.ok == OK, sign_in.ok
    assert sign_in.bad_request == BAD_REQUEST, sign_in.bad_request

    sign_out = SignOut(sign_in.token)
    sign_out.exec()

    assert sign_out.ok == OK, sign_in.token
    assert sign_out.bad_request == BAD_REQUEST, sign_out.bad_request
