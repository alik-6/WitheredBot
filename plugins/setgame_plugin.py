from discord.ext import commands
from discord import Game, Status
from libs.help import EmbedHelp
from libs.embed import Embed


class SetGame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setgame(self, ctx, name=""):
        """Set A Game As Your Activity"""
        if str(name).strip() == "":
            help = EmbedHelp(self.setgame, accepted_args=['Game'])
            await ctx.send(help())
        else:
            activity = Game(name=name, type=4)
            await self.bot.change_presence(status=Status.dnd, activity=activity)
            await ctx.send(Embed(title='Game Status', description=f"Using \"{name}\" as current game").create)


def setup(bot) -> dict:
    return {
        "Object": SetGame(bot),
        "name": "Custom Status",
        "description": "Adds Ability to Set Custom Games as you're status"
    }
