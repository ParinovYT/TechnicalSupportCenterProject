import datetime
from http.client import BAD_REQUEST, CONFLICT, OK, UNAUTHORIZED

from src.core.classes.mysql import MySqlBase
from src.core.classes.report import Report
from src.core.classes.user import User

USERNAME = 'user44_---'
PASSWORD = ')O#$VJ)#@MCO#N12V43nkjc32v'
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


class Create:
    def __init__(self, token: str) -> None:
        self.__ok = 0  # Set an initial value
        self.__bad_request = 0  # Set an initial value
        self.__token = token
        self.__unauthorized = 0

    @property
    def ok(self) -> int:
        return self.__ok

    @property
    def unauthorized(self) -> int:
        return self.__unauthorized

    @property
    def bad_request(self) -> int:
        return self.__bad_request

    def exec(self, inventory_number: str):
        user_obj = Report().create()
        user_obj.execute(self.__token, 'Issue', 'Issue Text', inventory_number)
        self.__ok = user_obj.status_code

        user_obj.execute('v23c423v3', '4342c342vv2343c2v4c424vc32v24c2343vc324c234vv', 'BMuLczvcFvASPN8ryybzKVkOut03PvruC', 1)
        self.__bad_request = user_obj.status_code

        user_obj.execute(
            'GnpQIcODM9hyQqM1dwNs1uxFnUr7VCJF445lbaDZlHmQVf7TRpYCfeS1IhTIM0Mel9OiS7XJJWDi15edYbL2Laf1Y5Tt0bMKm2oJ6me4NxtWgFmK81bKNFRC8v1aKOoGBB9lb7ZmsZ16iN6halzuz1mIAYQtBF07qgEkRlEg7TKFc9qNSQvHWPIV7ak0DVbrBVO7aHOkJnA50TGLjfTjkqoS54UI87j9Eiofe3n9cIekWdsIDVP90Dq0hXlOMXKG',
            '4342c342vv2343c2v4c424vc32v24c2343vc324c234vv', 'BMuLczvcFvASPN8ryybzKVkOut03PvruC',
            inventory_number
        )
        self.__unauthorized = user_obj.status_code


def get_device_id_by_inventory_number(value: str):
    """Temp solution"""
    db_connection = MySqlBase().connection()
    db_connection.open()
    try:
        cursor = db_connection.connection.cursor()

        # Используем параметризованный запрос
        cursor.execute("SELECT id FROM devices WHERE inventory_number=%s", (value,))

        row = cursor.fetchone()

        # Проверяем, есть ли результат
        if row:
            rule_id = int(row[0])
            return rule_id
        else:
            # Если не найдено, можно вернуть, например, None
            return 1
    finally:
        db_connection.close()


def create_device(inv_num: str):
    """Temp solution"""
    db_connection = MySqlBase().connection()
    db_connection.open()
    try:
        cursor = db_connection.connection.cursor(prepared=True, )
        insert_query = """
        INSERT INTO devices VALUES (NULL, %s, %s, %s, %s, %s, %s, %s);
        """
        params = (
            inv_num,
            'Компьютер',
            datetime.datetime(2006, 6, 5).isoformat(),
            3,
            '321', 
            'Персональный компьютер',
            'testUser'
        )

        cursor.execute(insert_query, params)
        db_connection.connection.commit()
    finally:
        db_connection.close()


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

    inventory_number = '4389CNV23CM8C'
    create_device(inventory_number)

    report_create = Create(sign_in.token)
    report_create.exec(inventory_number)

    assert report_create.ok == OK, report_create.ok
    assert report_create.bad_request == BAD_REQUEST, report_create.bad_request
    assert report_create.unauthorized == UNAUTHORIZED, report_create.unauthorized
