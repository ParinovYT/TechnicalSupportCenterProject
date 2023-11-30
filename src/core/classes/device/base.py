from typing import Any
from src.core.classes.mysql import MySqlBase
from src.core.classes.models.device import ModelDevice


class DeviceBase:
    def __init__(self):
        self._status_code: int
        self._DB = MySqlBase()
        self._model_device = ModelDevice()
        self._response = ModelDevice() 

    def execute(self) -> None:...