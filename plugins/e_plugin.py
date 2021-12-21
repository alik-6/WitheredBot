from discord.ext import commands
from requests import get

from help_func import EmbedHelp, msgf
from discord import Embed


class Init(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def explain(self, ctx, word=""):
        """Finds Meaning Online"""
        if str(word).strip() == "":
            help = EmbedHelp(self.explain, accepted_args=["Word"])
            await ctx.send(embed=await(help()))
        else:
            data = get(
                f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
            ).json()[0]
            definitions = data.get('meanings')[0].get('definitions')[0]
            e = Embed()
            if data.get('word'):
                word = data.get('word')
                e.title = word[0].upper() + word[1:]
            if definitions.get('definition'):
                e.description = msgf(f"[Q/]{definitions.get('definition')}")

            if definitions.get('example'):
                e.add_field(name="Example", value=msgf(f"[Q/]{definitions.get('example')}"))

            if definitions.get('synonyms'):
                e.add_field(name="Synonyms", value=msgf(f"[Q/]{', '.join(definitions.get('synonyms'))}"))
            if definitions.get('antonyms'):
                e.add_field(name="Antonyms", value=msgf(f"[Q/]{', '.join(definitions.get('antonyms'))}"))
            if data.get('meanings')[0].get('partOfSpeech'):
                e.add_field(name="Part of Speach", value=msgf(f"[Q/]{data.get('meanings')[0].get('partOfSpeech')}"))
            else:
                await ctx.send("unknown word")
            await ctx.send(embed=e)


def setup(bot) -> dict:
    return {
        "Object": Init(bot),
        "name": "Explain It",
        "description": "Adds Ability to use Dictionary Search"
    }
