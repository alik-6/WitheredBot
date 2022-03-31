import re
from requests import get
from discord.ext import commands
from libs.embed import Embed
from libs.help import EmbedHelp
from libs.extras import to_discord_str



class YoutubeSearch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def yt(self, ctx, *args):
        """Search The Youtube"""
        args = " ".join(args).replace(" ", "-")
        if args.strip() == "":
            help = EmbedHelp(self.yt, accepted_args=['Search'])
            await ctx.send(
                help()
            )
        else:
            message = await ctx.send(Embed(title="Youtube", description=f"searching for `{args}`").special)
            request_yt = get(
                f"https://www.youtube.com/results?search_query={args}"
            )
            yt_link = re.findall(r"watch\?v=(\S{11})", request_yt.content.decode())
            await message.delete()
            await ctx.send(
                to_discord_str(
                    f"[Q/][H]https://www.youtube.com/watch?v={yt_link[0]}[H]"
                )
            )


def setup(bot) -> dict:
    return {
        "Object": YoutubeSearch(bot),
        "name": "YouTube",
        "description": "Adds Ability to Search Youtube videos"
    }
