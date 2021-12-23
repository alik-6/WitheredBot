import re
from requests import get
from discord.ext import commands
from discord import Embed
from libs.help import EmbedHelp
from libs.extras import to_discord_str



class Init(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def yt(self, ctx, *args):
        """Search The Youtube"""
        args = " ".join(args).replace(" ", "-")
        if args.strip() == "":
            help = EmbedHelp(self.yt, accepted_args=['Search'])
            await ctx.send(
                embed=await(help())
            )
        else:
            message = await ctx.send(embed=Embed(title="Youtube", description=f"searching for `{args}`"))
            request_yt = get(
                f"https://www.youtube.com/results?search_query={args}"
            )
            yt_link = re.findall(r"watch\?v=(\S{11})", request_yt.content.decode())
            await message.delete()
            await ctx.send(
                content=to_discord_str(
                    f"[Q/][H]https://www.youtube.com/watch?v={yt_link[0]}[H]"
                ), embed=None
            )


def setup(bot) -> dict:
    return {
        "Object": Init(bot),
        "name": "YouTube",
        "description": "Adds Ability to Search Youtube videos"
    }
