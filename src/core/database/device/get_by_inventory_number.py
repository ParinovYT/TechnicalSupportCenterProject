from http.client import NOT_FOUND, OK
from src.core.classes.models.device import ModelDevice
from src.core.classes.mysql.queries import MySqlQuery
from src.core.database.connection import Connection
from mysql.connector.errors import Error


class GetByInventoryNumber(MySqlQuery):
    def __init__(self, connection: Connection, model_device: ModelDevice) -> None:
        super().__init__(connection)
        self.__model_device: ModelDevice = model_device
    
    @property
    def response(self) -> ModelDevice:
        return self.__model_device
    
    @property
    def status_code(self) -> int:
        return self._status_code

    def execute(self, inventory_number: str) -> None:
        try:
            cursor = self._connection.connection.cursor()

            cursor.execute("""
            SELECT id, inventory_number, object_name, year_issue, floor, office_number
            FROM devices
            WHERE inventory_number=%s
            """, (inventory_number,))

            row = cursor.fetchone()

            if row:
                self.__model_device.id = int(row[0])
                self.__model_device.inventory_number = str(row[1])
                self.__model_device.object_name = str(row[2])
                self.__model_device.year_issue = str(row[3])
                self.__model_device.floor = int(row[4])
                self.__model_device.office_number = str(row[5])
                
                self._status_code = OK
            else:
                self._status_code = NOT_FOUND

        except Error as e:
            self._status_code = NOT_FOUND
            print(e)