# [withered bot - v0.3]
from discord import Embed, errors
from discord.ext.commands import Bot
from libs.extras import to_discord_str, print
from libs.config import get, update
from load_plugins import LoadPlugin
from os import environ

bot = Bot(
    self_bot=True,
    command_prefix=get('prefix'),
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
            help_embed.add_field(name=f"{get('prefix')}{key}", value=to_discord_str(f"[L]{key.help}[L]"))

    await ctx.send(embed=help_embed)


@bot.event
async def on_command(ctx):
    command = ctx.command
    print(f'Command Executed: {command}')

@bot.command(aliases=['pl'])
async def plugins(ctx):
    e = Embed(title="Installed Plugins", description=f"{len(loaded_plugins)} plugins Installed")
    for i in loaded_plugins:
        e.add_field(name=i['name'], value=f"> {i['description']}", inline=False)
    e.set_footer(text=f"Load time: {globals()['load_time']}ms")
    await ctx.send(embed=e.set_thumbnail(url=ctx.author.avatar_url))


@bot.command()
async def about(ctx):
    await ctx.send(embed=Embed(
        title='About',
        description="`Written in python by` <@893794390164795392>"
    ).add_field(name="Github:", value="https://github.com/a-a-a-aa/WitheredBot").set_thumbnail(
        url=ctx.author.avatar_url)
    )


@bot.command()
async def setprefix(ctx, prefix=""):
    if prefix.strip():
        update('prefix', prefix)
        prefix = bot.command_prefix = get('prefix')
        await ctx.send(to_discord_str(f"[Q/]Prefix changed to [L]{prefix}[L]"))





# [loads the token from config and run's the bot]
def run_bot():
    try:
        token = get('token')
        if not token:
            token = str(environ['TOKEN'])

        bot.run(token, bot=False)
    except errors.LoginFailure:
        print("Improper Token: Are you sure you passed the right token?")

    except errors.DiscordServerError:
        print(
            "It looks like discord server are having some issues,please try again later status: "
            "https://discordstatus.com/")
    except errors.ConnectionClosed:
        print("Discord Unexpectedly Closed the connection")
    finally:
        pass


if __name__ == "__main__":
    pluginLoader = LoadPlugin(bot=bot)
    globals()['loaded_plugins'], globals()['load_time'] = pluginLoader.load_plugin()
    run_bot()
