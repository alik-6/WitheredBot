#[withered bot - v0.1]
import discord
from discord.ext.commands import Bot
from plugins.help_func import PREFIX
from os import listdir
import time
from importlib import import_module
from json import  load

bot = Bot(
        self_bot=True,
        command_prefix=PREFIX,
        help_command=None,
        case_insensitive=True
)


@bot.event
async def on_ready():
        print("[BOT] is ready")

#[loads plugins if any]
def load_plugin():
    t = time.time() * 1000
    for file in listdir('./plugins'):
            if file.endswith("_plugin.py"):
                try:
                    class_plug = import_module(f'plugins.{file.replace(".py", "")}')
                    bot.add_cog(eval("class_plug.setup(bot)"))
                    print(f"[ PLUGIN SYS ] `{file.replace('_plugin.py', '')}` Loaded Successfully")
                except ImportError:
                    print(f"[ PLUGIN SYS ] `{file.replace('_plugin.py', '')}` Failed to Load")
                finally:
                    pass
    print(f"Loaded All Plugins In {round(abs(t-time.time() * 1000))}ms")



#[loads the token from config and run's the bot]
def run_bot():
    with open('token.json', 'r') as token:
        try:
            TOKEN = load(token).get('token')
            bot.run(TOKEN , bot=False)
        except discord.errors.LoginFailure:
            print("===============Improper Token: Are you sure you passed the right token?===============")
        
        finally:
            pass


if __name__ == "__main__":
    load_plugin()
    run_bot()
