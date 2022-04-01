from discord.ext import (commands)
from libs.help import EmbedHelp
from libs.embed import Embed


class Calc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def calc(self, ctx, *args):
        """Caculates Basic Math"""
        args = " ".join(args)
        if args.strip() == "":
            help = EmbedHelp(self.calc, accepted_args=["Equation"])
            await ctx.send(help())
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
            await ctx.send(calc_embed.create)


def setup(bot) -> dict:
    return {
        "Object": Calc(bot),
        "name": "Calc",
        "description": "Adds the ability to do basic math"
    }
