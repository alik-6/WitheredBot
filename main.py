#[withered bot - v0.2]
from discord import Embed,errors
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

Loaded_cogs = []
@bot.event
async def on_ready():
        print("[BOT] is ready")


@bot.command()
async def help(ctx):
    excluded = ['help']
    help_embed = Embed(title="Help", description="List all commands")
    for key in bot.walk_commands():
        if str(key) not in excluded:
            help_embed.add_field(name=f"{PREFIX}{key}", value="`cmd`")

    await ctx.send(embed=help_embed)

@bot.command()
async def plugins(ctx):
    e = Embed(title="Installed Plugins", description=f"{len(Loaded_cogs)} plugins Installed")
    for i in Loaded_cogs:
        e.add_field(name=i['name'], value=f"> {i['description']}", inline=False)

    await ctx.send(embed=e.set_thumbnail(url=ctx.author.avatar_url))


@bot.command()
async def about(self, ctx):
        await ctx.send(embed=Embed(
            title="About",
            description="`Written in python by` <@893794390164795392>"
        ).add_field(name="Github:", value="https://github.com/a-a-a-aa/WitheredBot").set_thumbnail(url=ctx.author.avatar_url)
    )  

#[loads plugins if any]
def load_plugin():
    t = time.time() * 1000
    for file in listdir('./plugins'):
            if file.endswith("_plugin.py"):
                try:
                    class_plug = import_module(f'plugins.{file.replace(".py", "")}')
                    data = class_plug.setup(bot)
                    globals()['Loaded_cogs'].append(data)
                    bot.add_cog(data['Object'])
                    print(f"[ PLUGIN SYS ] `{data['name']}` Loaded Successfully")
                except ImportError:
                    print(f"[ PLUGIN SYS ] `{data['name']}` Failed to Load")
                finally:
                    pass
    print(f"Loaded All Plugins In {round(abs(t-time.time() * 1000))}ms")



#[loads the token from config and run's the bot]
def run_bot():
    with open('token.json', 'r') as token:
        try:
            TOKEN = load(token).get('token')
            bot.run(TOKEN , bot=False)
        except errors.LoginFailure:
            print("===============Improper Token: Are you sure you passed the right token?===============")
        
        except errors.DiscordServerError:
            print("It looks like discord server are having some issues,please try again later status: https://discordstatus.com/")
        except errors.ConnectionClosed:
            print("Discrod Unexpectidly Closed the connection")
        finally:
            pass

if __name__ == "__main__":
    load_plugin()
    run_bot()
