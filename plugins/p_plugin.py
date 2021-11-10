import os

import discord
from discord.ext import commands
from .help_func import embed_help
import psutil


class P(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ps(self, ctx, *args):
        args = "".join(args)
        if args.strip() == "":
            await ctx.send(embed=await (
                embed_help(help=f"ps [arg]", accepted_args=['kill', 'list'], usage="Manage system's processes")))
        if args.strip() == "list":
            list_embed = "```"
            for proc in psutil.process_iter():
                try:
                    list_embed += f"{proc.pid} {str(proc.name()).replace('.exe', '').strip()}\n"
                except:
                    await ctx.send("```Error for some reason xD```")

            list_embed += "```"
            await ctx.send(embed=discord.Embed(title='Running Processes', description=list_embed))



        if args.startswith('kill'):
            pid = args.replace('kill', '').strip()
            if pid != "":
                try:
                    os.kill(int(pid), 9)
                    await ctx.send(
                        embed=discord.Embed(title="Killed Process", description=f"killed process with pid: {pid}"))
                except:
                    await ctx.send(embed=discord.Embed(title="Error Raised", description="Error ending PROCESS"))
                finally:
                    pass
            else:
                await ctx.send(
                    embed=await(embed_help(help="ps kill [arg]", accepted_args=["process"], usage="kills an process"))
                )


def setup(bot):
    return P(bot)
