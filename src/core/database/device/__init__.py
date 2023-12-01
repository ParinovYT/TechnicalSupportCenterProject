from src.core.classes.models.device import ModelDevice
from src.core.classes.mysql.queries import MySqlQuery
from src.core.database.connection import Connection
from src.core.database.device.get_by_inventory_number import GetByInventoryNumber


class Device:
    def __init__(self, connection: Connection, model_device: ModelDevice) -> None:
        self.__connection: Connection = connection
        self.__model_device: ModelDevice = model_device

    def get_by_inventory_number(self):
        obj: MySqlQuery = GetByInventoryNumber(self.__connection, self.__model_device)
        return obj
