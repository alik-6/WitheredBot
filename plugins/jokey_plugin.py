from libs.embed import (Embed)
from discord.ext import (commands)
from requests import get


class Joke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joke(self, ctx):
        params: dict[str] = {}
        params.update({'blacklistFlags': 'nsfw'})
        params.update({'type': 'single'})
        request = get('https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Dark,Pun,Spooky?type=single', params=params).json()
        if not request['error']:
            joke = Embed(
                title=f"{request['category']}",
                description=f"{request['joke']}"
            )

            await ctx.send(joke.create)
        else:
            error = Embed(
                title="Error",
                description="Api is unavailable"
            )
            await ctx.send(error.create)


def setup(bot) -> dict:
    return {
        "Object": Joke(bot),
        "name": "Jokey",
        "description": "Gets a joke :wink:",
    }
