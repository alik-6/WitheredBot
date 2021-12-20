from discord.ext import commands
import asyncio
from random import randint
from help_func import aprint


class Init(commands.Cog):
    def __init__(self,  bot):
        self.bot = bot
        self.stop_bot = False

    async def sleep(self, i: int):
        while i != 0:
            if self.stop_bot:
                aprint("Broke Sleep Loop")
                break
            else:
                await asyncio.sleep(1)
                aprint(f"Run again in {i}s")
                i -= 1

    @commands.command()
    async def stopowo(self, ctx):
        """Stops The Mining"""
        await ctx.message.delete()
        await ctx.send('> `Stopped the minning`')
        self.stop_bot = True

    @commands.command(pass_context=True)
    async def startowo(self, ctx, channel_id=None):
        """Start The OwO mining"""
        async def mine(c_id):
            await ctx.message.delete()
            await ctx.send(':pick: started')
            self.stop_bot = False
            channel = self.bot.get_channel(int(c_id))
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

        if channel_id is None:
            await mine(ctx.channel.id)
        else:
            await mine(channel_id)
            

def setup(bot) -> dict:
    return {"Object": Init(bot), "name": "OwOminie", "description": "Adds ability to Mine OwO coins "}
