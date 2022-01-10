# [loads plugins if any]
from importlib import import_module
from os import listdir
import time
from libs.config import set, get
from libs.extras import print

class LoadPlugin:
    def __init__(self, bot):
        self.bot = bot
        self.load_time = 0
        self.loaded = []
    def required_keys(self, data):
        if data.get('required_keys'):
            for i in data['required_keys']:
                if not get(i):
                    rk = input(f'Required KEY {i} >\n This Plugin Requires The Following Values To be Added \n Enter {i}: ')
                    if rk:
                        set(i, rk)
                    else:
                        print('Imvalid Value Exiting')
                        quit(0)
    
    def load_plugin(self):
        for file in listdir("./plugins"):
            t = time.time() * 1000
            if file.endswith("_plugin.py"):
                try:
                    class_plug = import_module(f'plugins.{file.replace(".py", "")}')
                    data = class_plug.setup(self.bot)
                    self.required_keys(data)
                    self.bot.add_cog(data['Object'])
                    self.load_time += round(abs(t - time.time() * 1000))
                    self.loaded.append(data)
                    print(f"Plugin \"{data['name']}\" Loaded!")
                except ImportError:
                    print(f"Plugin Loading Failed!")
                finally:
                    pass
        print(f"Loaded All Plugins In {self.load_time}ms")
        return self.loaded