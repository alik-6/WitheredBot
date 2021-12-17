from discord.ext import commands
from discord import Game, Status
from help_func import embed_help, msgf


class Init(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setgame(self, ctx, name=""):
        if str(name).strip() == "":
            await ctx.send(embed=await (embed_help("setgame [Game]")))
        else:
            activity = Game(name=name, type=4)
            await self.bot.change_presence(status=Status.dnd, activity=activity)
            await ctx.send(msgf(f"[B]{name}[B] set as default game"))


def setup(bot) -> dict:
    return {"Object": Init(bot), "name": "Custom Status", "description": "Adds Ability to Set Custom Games as you're status"}
