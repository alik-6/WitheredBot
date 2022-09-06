from discord.ext import commands
from libs.help import EmbedHelp
from libs.extras import to_discord_str
from random import choice
from libs.embed import Embed
from typing import Any


class FlipnFormat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def flip(self, ctx):
        """Flips The Coin"""
        flip_embed = Embed(
            title="Flipping the coin",
            description=f"{choice(['Head', 'Tail'])} wins"
        )
        await ctx.send(flip_embed.create)

    @commands.command()
    async def fmt(self, ctx, *msg):
        """Formats The String"""
        args = " ".join(msg)
        if args.strip() == "":
            help = EmbedHelp(self.fmt, accepted_args=['message'])
            await ctx.send(
                help()
            )
        else:
            await ctx.message.delete()
            await ctx.send(to_discord_str(args))


def setup(bot) -> dict[str, Any]:
    return {
        "Object": FlipnFormat(bot),
        "name": "Formatter",
        "description": "Adds Ability to Format Messages"
    }
