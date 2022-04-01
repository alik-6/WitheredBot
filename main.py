# [withered bot - v0.4]
from discord import errors
from libs.embed import Embed
from discord.ext.commands import Bot, Context
from libs.extras import to_discord_str, print
from libs.config import get, update, set

from load_plugins import LoadPlugin

bot = Bot(
    self_bot=True,
    command_prefix=get('PREFIX'),
    help_command=None,
    case_insensitive=True
)

load_time = 0
loaded_plugins = []


@bot.event
async def on_ready():
    print("Started")


@bot.command()
async def help(ctx):
    excluded = ['help']
    help_embed = Embed(title="Help", description="List all commands")
    for key in bot.walk_commands():
        if str(key) not in excluded:
            help_embed.add_field(name=f"{get('PREFIX')}{key}", value=f"{key.help}")

    await ctx.send(help_embed.create)


@bot.event
async def on_command(ctx: Context):
    command = ctx.command

    print(f'Command Executed: {command}')


@bot.command(aliases=['pl'])
async def plugins(ctx):
    embed = Embed(title="Installed Plugins", description=f"{len(loaded_plugins)} plugins Installed")
    for plugin in loaded_plugins:
        embed.add_field(name=plugin['name'], value=f"> {plugin['description']}", inline=False)
    embed.set_footer(text=f"Load time: {globals()['load_time']}ms")
    await ctx.send(embed.create)


@bot.command()
async def about(ctx):
    embed = Embed(
        title='About',
        description="`Written in python by` <@893794390164795392>"
    )
    embed.add_field(name="Github:", value="https://github.com/a-a-a-aa/WitheredBot")
    await ctx.send(
        embed.create
    )


@bot.command()
async def setprefix(ctx, prefix=""):
    if prefix.strip():
        update('prefix', prefix)
        prefix = bot.command_prefix = get('prefix')
        await ctx.send(to_discord_str(f"[Q/]Prefix changed to [L]{prefix}[L]"))


def run_bot():
    try:
        token = get('TOKEN')
        prefix = get('PREFIX')
        if not token:
            set('TOKEN', input('Enter TOKEN>'))
        if not prefix:
            set('PREFIX', input('Enter PREFIX>'))
        bot.run(get('TOKEN'), bot=False)
    except errors.LoginFailure:
        print("Improper Token: Are you sure you passed the right token?")
        set('TOKEN', '')
    except errors.DiscordServerError:
        print("It looks like discord server are having some issues,please try again later status: "
              "https://discordstatus.com/")
    except errors.ConnectionClosed:
        print("Discord Unexpectedly Closed the connection")


if __name__ == "__main__":
    pluginLoader = LoadPlugin(bot=bot)
    globals()['loaded_plugins'], globals()['load_time'] = pluginLoader.load_plugin()
    run_bot()
