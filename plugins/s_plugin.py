from discord.ext import commands
from discord import Game, Status
from help_func import EmbedHelp, msgf


class Init(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setgame(self, ctx, name=""):
        """Set A Game As Your Activity"""
        if str(name).strip() == "":
            help = EmbedHelp(self.setgame, accepted_args=['Game'])
            await ctx.send(embed=await(help()))
        else:
            activity = Game(name=name, type=4)
            await self.bot.change_presence(status=Status.dnd, activity=activity)
            await ctx.send(msgf(f"[B]{name}[B] set as default game"))


def setup(bot) -> dict:
    return {
        "Object": Init(bot),
        "name": "Custom Status",
        "description": "Adds Ability to Set Custom Games as you're status"
    }
