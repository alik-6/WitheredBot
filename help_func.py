import time, sys
from discord import (Embed, Colour)
from json import loads


def cfg():
    with open('config.json', 'r') as file:
        f = loads(file.read())

    return f


PREFIX = cfg()['prefix']


async def embed_help(parant, accepted_args=[]):
    embed = Embed(
        title="Usage"
    )
    if accepted_args:
        description = f"[C]{PREFIX}{parant.name}"
        for i in accepted_args:
            description += f" [{i}]"
        embed.description = msgf(description + "[C]")
        accepted_args = ', '.join(accepted_args)
        embed.add_field(name="Args", value=msgf(f"[C]{accepted_args}[C]"))
    if parant.help:
        embed.add_field(name=f"Help", value=msgf(f"[C]{parant.help}[C]"))
    if parant.aliases:
        embed.add_field(name="Aliases", value=msgf(f"[C]{', '.join(parant.aliases)}[C]"))
    return embed


def msgf(s):
    format_info = {
        "[B]": "**",
        "[I]": "*",
        "[H]": "||",
        "[C]": "```",
        "[L]": "`",
        "[Q/]": "> ",
    }
    sk = []
    for key, val in format_info.items():
        if key in s:
            s = s.replace(key, val)
    sk = s
    return sk


def aprint(animation):
    temp_str = "[ BOT ] "
    for i in animation:
        temp_str += i
        time.sleep(0.01)
        sys.stdout.write("\r" + temp_str)
        sys.stdout.flush()
    sys.stdout.write("\n")
