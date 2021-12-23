import json
from os import path


class BotConfig:
    def __init__(self):
        self.config_name = 'config.json'
        self.config = self.load()

    def load(self):
        if path.exists(self.config_name):
            with open(self.config_name, 'r') as r:
                return json.loads(r.read())
        else:
            raise Exception("No Config file Found")

    def get(self, name):
        if name in self.config:
            return self.config.get(name)
        else:
            raise Exception(f"json['{name}'] key doesn't exists")

    def write(self):
        with open(self.config_name, 'w') as w:
            w.write(json.dumps(self.config))

    def change(self, name, value):
        if name in self.config:
            self.config[name] = value
            self.write()
        else:
            raise Exception(f"json['{name}'] key doesn't exists")

    def add(self, name, value):
        if name in self.config:
            raise Exception(f"json['{name}'] already exists")
        else:
            self.config[name] = value
            self.write()

    def delete(self, name):
        if name in self.config and name in ['prefix', 'token']:
            raise Exception(f"json['{name}'] cannot delete key")
        if name not in self.config:
            raise Exception(f"json['{name}'] key doesn't exist")
        else:
            del self.config[name]
            self.write()
