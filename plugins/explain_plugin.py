from email import message
from turtle import title
from discord.ext import commands
from requests import get
from libs.help import EmbedHelp
from libs.embed import Embed
from typing import Any


class Explain(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def explain(self, ctx, word=""):
        """Finds Meaning Online"""
        if str(word).strip() == "":
            help = EmbedHelp(self.explain, accepted_args=["Word"])
            await ctx.send(help())
        else:
            embed = Embed()
            payload = get(
                f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
            ).json()
            if not isinstance(payload, list) and payload.get('title'):
                embed.title = payload.get('title')
                embed.description = payload.get('message')
            else:
                payload = payload[0]
                definitions = payload.get('meanings')[0].get('definitions')[0]
                if payload.get('word'):
                    word = payload.get('word')
                    embed.title = word[0].upper() + word[1:]

                elif definitions.get('definition'):
                    embed.description = f"{definitions.get('definition')}"

                elif definitions.get('example'):
                    embed.add_field(
                        name="Example", value=f"{definitions.get('example')}")

                elif definitions.get('synonyms'):
                    embed.add_field(
                        name="Synonyms", value=f"{', '.join(definitions.get('synonyms'))}")
                elif definitions.get('antonyms'):
                    embed.add_field(
                        name="Antonyms", value=f"{', '.join(definitions.get('antonyms'))}")
                elif payload.get('meanings')[0].get('partOfSpeech'):
                    embed.add_field(
                        name="Part of Speach", value=f"{payload.get('meanings')[0].get('partOfSpeech')}")

            await ctx.send(embed())


def setup(bot) -> dict[str, Any]:
    return {
        "Object": Explain(bot),
        "name": "Explain It",
        "description": "Adds Ability to use Dictionary Search"
    }
