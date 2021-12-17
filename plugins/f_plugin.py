from discord.ext import commands
from help_func import embed_help, msgf
from random import choice
from discord import Embed


class Init(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def flip(self, ctx):
        await ctx.send(
            embed=Embed(
                title="Flipping the coin",
                description=msgf(f"[B]{choice(['Head', 'Tail'])}[B] wins"),
            )
        )

    @commands.command()
    async def fmt(self, ctx, *msg):
        args = " ".join(msg)
        if args.strip() == "":
            await ctx.send(
                embed=await(embed_help(f"fmt [arg]", accepted_args=['message'], usage="Format the message")))
        await ctx.message.delete()
        await ctx.send(msgf(args))


def setup(bot) -> dict:
    return {"Object": Init(bot), "name": "Formatter", "description": "Adds Ability to Format Messages"}

