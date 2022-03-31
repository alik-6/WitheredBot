from libs.extras import to_discord_str
from discord.ext import (commands)


class Afk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.afk = False

    @commands.Cog.listener()
    async def on_message(self, message):
        is_afk = self.afk
        if not message.guild and message.author != self.bot.user and is_afk:
            await message.channel.send(to_discord_str('[C][BOT] Sorry I am Afk rn[C]'))
        if message.guild and is_afk and message.author != self.bot.user:
            for message_obj in message.mentions:
                if message_obj.id == self.bot.user.id:
                    await message.channel.send(to_discord_str('[C][BOT] Sorry I am Afk rn[C]'))

    @commands.command()
    async def afk(self, ctx):
        """Toggle Afk Mode"""
        if self.afk:
            await ctx.send(to_discord_str('[Q/][BOT] Not Afk Anymore'))
            self.afk = False
            # break
        else:
            await ctx.send(to_discord_str('[Q/][BOT]  Afk system activated '))
            self.afk = True


def setup(bot) -> dict:
    return {
        "Object": Afk(bot),
        "name": "Afk",
        "description": "Adds ability to use afk system"
    }
