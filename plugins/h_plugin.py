from discord.ext import commands
from discord import Embed
from .help_func import PREFIX


class H(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        excluded = ['help']
        help_embed = Embed(title="Help", description="List all commands")
        for key in self.bot.walk_commands():
            if str(key) not in excluded:
                help_embed.add_field(name=f"{PREFIX}{key}", value="`cmd`")

        await ctx.send(embed=help_embed)


def setup(bot):
    return H(bot)