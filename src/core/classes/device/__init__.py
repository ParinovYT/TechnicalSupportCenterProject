from src.core.device import DeviceGetByInventoryNumber
from src.core.classes.device.base import DeviceBase


class Device:
    def __init__(self) -> None:...

    def get_by_inventory_number(self):
        obj: DeviceBase = DeviceGetByInventoryNumber()
        return obj
