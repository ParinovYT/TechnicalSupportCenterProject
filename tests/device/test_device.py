import datetime
from http.client import NOT_FOUND, OK
from typing import Any
from src.core.classes.models.device import ModelDevice
from src.core.classes.user import User
from src.core.classes.mysql import MySqlBase

INVENTORY_NUMBER = '#34V23BVV'
OBJECT_NAME = 'Принтер'
YEAR_ISSUE = datetime.datetime(2020, 10, 23).isoformat()
FLOOR = 3
OFFICE_NUMBER = '341'

def create_device(inv_num: str):
    """Temp solution"""
    db_connection = MySqlBase().connection()
    db_connection.open()
    try:
        cursor = db_connection.connection.cursor(prepared=True,)
        insert_query = """
        INSERT INTO devices VALUES (NULL, %s, %s, %s, %s, %s);
        """
        params = (
            inv_num,
            OBJECT_NAME,
            YEAR_ISSUE,
            FLOOR,
            OFFICE_NUMBER
        )

        cursor.execute(insert_query, params)
        db_connection.connection.commit()
    finally:
        db_connection.close()

class GetDivece:
    def __init__(self) -> None:
        self.__ok = 0
        self.__not_found = 0
        self.__resp: ModelDevice

    @property
    def resp(self) -> ModelDevice:
        return self.__resp

    @property
    def ok(self) -> int:
        return self.__ok

    @property
    def not_found(self) -> int:
        return self.__not_found

    def exec(self):
        user_obj = User().device().get_by_inventory_number()
        user_obj.execute(INVENTORY_NUMBER)
        self.__ok = user_obj.status_code
        self.__resp = user_obj.response

        user_obj.execute('123')
        self.__not_found = user_obj.status_code

def test_device():
    create_device(INVENTORY_NUMBER)

    get_device = GetDivece()
    get_device.exec()

    assert get_device.ok == OK, get_device.resp.id
    assert get_device.resp.object_name == OBJECT_NAME, get_device.resp.object_name
    assert get_device.not_found == NOT_FOUND, get_device.not_found
