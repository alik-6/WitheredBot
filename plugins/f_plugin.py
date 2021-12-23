from discord.ext import commands
from libs.help import EmbedHelp, to_discord_str
from random import choice
from discord import Embed


class Init(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def flip(self, ctx):
        """Flips The Coin"""
        await ctx.send(
            embed=Embed(
                title="Flipping the coin",
                description=to_discord_str(f"[B]{choice(['Head', 'Tail'])}[B] wins"),
            )
        )

    @commands.command(aliases=["format"])
    async def fmt(self, ctx, *msg):
        """Formats The String"""
        args = " ".join(msg)
        if args.strip() == "":
            help = EmbedHelp(self.fmt, accepted_args=['message'])
            await ctx.send(
                embed=await(help())
            )
        else:
            await ctx.message.delete()
            await ctx.send(to_discord_str(args))


def setup(bot) -> dict:
    return {
        "Object": Init(bot),
        "name": "Formatter",
        "description": "Adds Ability to Format Messages"
    }
