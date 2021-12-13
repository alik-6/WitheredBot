from discord.ext import (commands)
from .help_func import embed_help
from discord import (Embed)


class Init(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def calc(self, ctx, *args):
        args = " ".join(args)
        if args.strip() == "":
            await ctx.send(embed=await (embed_help(f"calc [Equation]")))
        else:
            try:
                calc_embed = Embed(title="Result", description=f"{args} = {eval(args)}")
            except ValueError:
                calc_embed = Embed(title="Error", description=f"Invalid equation: {args}")
            except ZeroDivisionError:
                calc_embed = Embed(title="Error", description=f"Can't Divide Zero by itself: {args}")
            except SyntaxError:
                calc_embed = Embed(
                    title="Error", description=f"Invalid syntax: {args}"
                )
            await ctx.send(embed=calc_embed)


def setup(bot) -> dict:
    return {"Object": Init(bot), "name": "Calc", "description": "Adds the ability to do basic math"}
