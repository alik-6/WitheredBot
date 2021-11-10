from discord.ext import commands
from .help_func import embed_help, msgf
from asyncio import  sleep


class R(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def repeat(self, ctx, message="", num=1):
        if message.strip() == "":
            await ctx.send(embed=await (embed_help("repeat [message] [number]")))
            return
        if num > 200:
            await ctx.send(embed=await (embed_help("Must be less then 30")))
        else:
            for _ in range(num):
                await sleep(0.8)
                await ctx.send(msgf(message))


def setup(bot):
    return R(bot)