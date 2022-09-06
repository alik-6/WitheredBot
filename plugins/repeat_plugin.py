from discord.ext import commands
from libs.help import EmbedHelp
from libs.extras import to_discord_str
from asyncio import sleep
from typing import Any


class Repeat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def repeat(self, ctx, num=2, delay=0.8, *message):
        """Repeats | Spam a message"""
        message = " ".join(message)

        if message.strip() == "" or num <= 0 or delay < 0.8:
            help = EmbedHelp(self.repeat, accepted_args=[
                             "number", "delay", "message"])
            await ctx.send(help())
        else:
            has_counter = False
            if message.find('${C}') != -1:
                has_counter = True
            for x in range(num):
                await sleep(delay)
                await ctx.send(to_discord_str([message if not has_counter
                                               else message.replace('${C}', str(x + 1))
                                               ][0]))


def setup(bot) -> dict[str, Any]:
    return {
        "Object": Repeat(bot),
        "name": "Repeat it!",
        "description": "Adds Ability to Repeat|Spam a Message"
    }
