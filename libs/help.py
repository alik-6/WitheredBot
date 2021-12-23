import sys
import time
from json import loads

from discord import Embed


def cfg():
    with open('config.json', 'r') as file:
        f = loads(file.read())

    return f


def get_prefix():
    return cfg()['prefix']


def print(animation):
    temp_str = "[ BOT ] "
    for i in animation:
        temp_str += i
        time.sleep(0.01)
        sys.stdout.write("\r" + temp_str)
        sys.stdout.flush()
    sys.stdout.write("\n")


class EmbedHelp:
    def __init__(self, parent, accepted_args=None):
        self.parent = parent
        self.accepted_args = accepted_args

    async def __call__(self):
        embed = Embed(
            title="Usage"
        )
        if self.accepted_args:
            description = f"[C]{get_prefix()}{self.parent.name}"
            for i in self.accepted_args:
                description += f" [{i}]"
                embed.description = to_discord_str(description + "[C]")
                self.accepted_args = ', '.join(self.accepted_args)
                embed.add_field(name="Args", value=to_discord_str(f"[C]{self.accepted_args}[C]"))
        if self.parent.help:
            embed.add_field(name=f"Help", value=to_discord_str(f"[C]{self.parent.help}[C]"))
        if self.parent.aliases:
            embed.add_field(name="Aliases", value=to_discord_str(f"[C]{', '.join(self.parent.aliases)}[C]"))

        return embed

    def __repr__(self):
        print(f"({self.parent}, {self.accepted_args})")


def to_discord_str(s):
    format_info = {
        "[B]": "**",
        "[I]": "*",
        "[H]": "||",
        "[C]": "```",
        "[L]": "`",
        "[Q/]": "> ",
    }

    for key, val in format_info.items():
        if key in s:
            s = s.replace(key, val)
    sk = s
    return sk
