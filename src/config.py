import json

class Config:
    _instance = None
    get = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def Load(path: str = 'src/config.json'):
        cfg = 0
        if Config.get == 0:
            with open(path) as f:
                cfg = json.load(f)
        Config.get = cfg
