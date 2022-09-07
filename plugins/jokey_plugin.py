from libs.embed import (Embed)
from discord.ext import (commands)
from requests import get
from typing import Any


class Joke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joke(self, ctx):

        params: dict[str] = {}
        params.update({'blacklistFlags': 'nsfw'})
        params.update({'type': 'single'})
        request = get(
            'https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Pun,Spooky', params=params).json()
        if not request['error']:
            joke = Embed(
                title=f"{request['category']}",
                description=f"{request['joke']}"
            )

            await ctx.send(joke())
        else:
            error = Embed(
                title="Error",
                description="Api is unavailable"
            )
            await ctx.send(error())


def setup(bot) -> dict[str, Any]:
    return {
        "Object": Joke(bot),
        "name": "Jokey",
        "description": "Gets a joke :wink:",
    }
