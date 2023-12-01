from http.client import NOT_FOUND

from src.core.classes.device.base import DeviceBase
from src.core.classes.models.device import ModelDevice
from src.core.database.device import Device


class DeviceGetByInventoryNumber(DeviceBase):
    def __init__(self):
        super().__init__()

    @property
    def status_code(self) -> int:
        return self._status_code

    @property
    def response(self) -> ModelDevice:
        return self._response

    def execute(self, inventory_number: str) -> None:
        MySQl = self._DB
        db_connection = MySQl.connection()
        MySQlQueries = MySQl.queries()

        try:
            db_connection.open()
            MySQlQueries = MySQl.queries()
            query_user_info: MySQlQueries = Device(db_connection, self._model_device).get_by_inventory_number()

            query_user_info.execute(inventory_number)
            self._response = query_user_info.response
            self._status_code = query_user_info.status_code

        except Exception as e:
            print(e)
            self._status_code = NOT_FOUND

        finally:
            db_connection.close()
