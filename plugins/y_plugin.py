import re
from requests import get
from discord.ext import commands

from .help_func import embed_help, msgf


class R(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def yt(self, ctx, *args):
        args = " ".join(args).replace(" ", "-")
        if args.strip() == "":
            await ctx.send(
                embed=await (embed_help(f"yt [arg]", accepted_args=['search'], usage="search youtube for stuff")))
        else:
            request_yt = get(
                f"https://www.youtube.com/results?search_query={args}"
            )
            yt_link = re.findall(r"watch\?v=(\S{11})", request_yt.content.decode())
            await ctx.send(
                msgf(
                    f"[Q/][H]https://www.youtube.com/watch?v={yt_link[0]}[H]"
                )
            )


def setup(bot):
    return R(bot)
