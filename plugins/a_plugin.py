from help_func import embed_help, msgf
from discord import (Embed)
from art import text2art
from discord.ext import (commands)


class Init(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.afk = False

    @commands.Cog.listener()
    async def on_message(self, message):
        is_afk = self.afk
        if not message.guild and message.author != self.bot.user and is_afk:
            await message.channel.send(msgf('[C][BOT] Sorry I am Afk rn[C]'))
        if message.guild and is_afk and message.author != self.bot.user:
            for message_obj in message.mentions:
                if message_obj.id == self.bot.user.id:
                    await message.channel.send(msgf('[C][BOT] Sorry I am Afk rn[C]'))

    @commands.command()
    async def afk(self, ctx):
        if self.afk:
            await ctx.send(msgf('[Q/][BOT] Not Afk Anymore'))
            self.afk = False
            # break
        else:
            await ctx.send(msgf('[Q/][BOT]  Afk system activated '))
            self.afk = True

    @commands.command()
    async def art(self, ctx, *args):
        args = " ".join(args)
        if args.strip() == "":
            await ctx.send(embed=await (embed_help("art [Word]")))
        else:
            embed = Embed(title="Art")
            if len(args) < 7:
                art = text2art(args)
                embed.description = msgf(f"[C]{art}[C]")
            else:
                embed.description = msgf("[C]Must be less than 7 alphabets[C]")
            await ctx.send(embed=embed)


def setup(bot) -> dict:
    return {"Object": Init(bot), "name": "Aro", "description": "Adds ability to use ascii art and afk system"}
