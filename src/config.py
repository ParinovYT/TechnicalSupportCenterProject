import json

class Config:
    _instance = None
    _get = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance

    @classmethod
    def get(cls, text, path: str = 'src/config.json'):
        if cls._get == 0:
            with open(path) as f:
                cls._get = json.load(f)
        return cls._get[text]
