import json

data = 0


def load_configurate(file: str):
    global data
    with open(file) as f:
        data = json.load(f)

    return data
