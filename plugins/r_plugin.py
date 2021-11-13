from discord.ext import commands
from .help_func import embed_help, msgf
from asyncio import  sleep


class R(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def repeat(self, ctx, *message):
        message = " ".join(message)
        num = int(message.split('x')[-1]) | 1
       
        if message.strip() == "":
            await ctx.send(embed=await(embed_help("repeat [message]x[number]")))
            return
        if num > 200:
            await ctx.send(embed=await(embed_help("Must be less then 30")))
        else:
            msg_to_send = message.strip(f"x{num}")
            for _ in range(num):
                await sleep(0.8)        
                await ctx.send(msgf(msg_to_send))


def setup(bot):
    return R(bot)
