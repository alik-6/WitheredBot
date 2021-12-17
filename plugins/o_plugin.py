from discord.ext import commands
import asyncio
from random import randint

from .help_func import aprint



class Init(commands.Cog):
    def __init__(self,  bot):
        self.bot = bot
        self.stop_bot = False

    async def sleep(self, i: int):
        while i != 0:
            if self.stop_bot == True: 
                aprint("Broke Sleep Loop")
                break
            else:
                await asyncio.sleep(1)
                aprint(f"Run again in {i}s")
                i -= 1

    @commands.command()
    async def stopmineowo(self, ctx):
        await ctx.message.delete()
        await ctx.send('> `Stopped the minning`')
        self.stop_bot = True

    @commands.command(pass_context=True)
    async def letsmineowo(self, ctx, channelid=None):
        async def mine(id):
            await ctx.message.delete()
            await ctx.send(':pick: started')
            self.stop_bot = False
            channel = self.bot.get_channel(int(id))
            while not self.stop_bot:
                async with ctx.typing():
                    aprint("[BOT] Running Batch")
                    await self.sleep(randint(5, 15))
                    await channel.send('owoh')
                    
                    await self.sleep(randint(5, 12))
                    await channel.send('owo sell all')
                    await self.sleep(randint(5, 16))
                    await channel.send('owo cash')
                    sleep_time = 50 + randint(20,30) 
                    await self.sleep(sleep_time)

        if channelid == None:
            await mine(ctx.channel.id)
        else:
            await mine(channelid)
            



def setup(bot) -> dict:
    return {"Object": Init(bot), "name": "OwOminie", "description": "Adds ability to Mine OwO coins "}
