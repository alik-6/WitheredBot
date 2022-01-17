from libs.help import EmbedHelp
from discord import (Embed)
from discord.ext import (commands)
from requests import get


class Init(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joke(self, ctx, nsfw = ""):
        params={}
        if nsfw:
            params.update({'blacklistFlags': 'nsfw'})
        params.update({'type': 'single'})
        request = get('https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Dark,Pun,Spooky?type=single', params=params).json()
        if not request['error']:
            await ctx.send(embed=Embed(
                title=f"{request['category']}", 
                description=f"{request['joke']}"
            ))
        else:
            await ctx.send(embed=Embed(
                title="Error",
                description="Api is unavailable"
            ))


def setup(bot) -> dict:
    return {
        "Object": Init(bot),
        "name": "Jokey",
        "description": "Gets a joke :wink:",
    }
