from src.core.classes.models.device import ModelDevice
from src.core.classes.mysql import MySqlBase


class DeviceBase:
    def __init__(self):
        self._status_code: int
        self._DB = MySqlBase()
        self._model_device = ModelDevice()
        self._response = ModelDevice()

    def execute(self) -> None: ...
