from datetime import date, datetime, timezone
from discord.ext import commands
from discord import Game, Status
from discord.activity import Game
from libs.help import EmbedHelp
from libs.embed import Embed
from typing import Any


class SetGame(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def setgame(self, ctx, name=""):
        """Set A Game As Your Activity"""
        if str(name).strip() == "":
            help = EmbedHelp(self.setgame, accepted_args=['Game'])
            await ctx.send(help())
        else:
            activity = Game(name=name, type=4,
                            start=datetime.now(timezone.utc))

            await self.bot.change_presence(status=Status.dnd, activity=activity)
            statusEmbed = Embed(title='Game Status',
                           description=f"Using \"{name}\" as current game")
            await ctx.send(statusEmbed())


def setup(bot) -> dict[str, Any]:
    return {
        "Object": SetGame(bot),
        "name": "Custom Status",
        "description": "Adds Ability to Set Custom Games as you're status"
    }
