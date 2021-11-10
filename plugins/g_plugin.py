from discord.ext import commands
from discord import Game, Status
from .help_func import embed_help, msgf


class G(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gameset(self, ctx, name=""):
        if str(name).strip() == "":
            await ctx.send(embed=await (embed_help("gameset [Game]")))
        else:
            activity = Game(name=name, type=4)
            await self.bot.change_presence(status=Status.dnd, activity=activity)
            await ctx.send(msgf(f"[B]{name}[B] set as default game"))


def setup(bot):
    return G(bot)
