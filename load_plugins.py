# [loads plugins if any]
from importlib import import_module
from os import listdir
import time
from libs.extras import print


class LoadPlugin:
    def __init__(self, bot):
        self.bot = bot

    def load_plugins(self):
        load_time = 0
        _loaded_plugins: list[dict] = []
        for file in listdir("./plugins"):
            if file.endswith("_plugin.py"):
                try:
                    plugin_load_start = time.time() * 1000
                    class_plug = import_module(
                        f'plugins.{file.replace(".py", "")}')
                    data = class_plug.setup(self.bot)
                    self.bot.add_cog(data.get('Object'))
                    load_time += round(abs(plugin_load_start -
                                       time.time() * 1000))
                    _loaded_plugins.append(data)
                    print(f"Plugin \"{data.get('name')}\" Loaded!")
                except ImportError:
                    print(f"Plugin Loading Failed!")
                finally:
                    pass

        print(f"Loaded All Plugins In {load_time}ms")
        return {"LoadedPlugins": _loaded_plugins, "LoadTime": load_time}
