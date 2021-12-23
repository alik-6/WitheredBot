import time, sys


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


def print(animation):
    temp_str = "[ BOT ] "
    for i in animation:
        temp_str += i
        time.sleep(0.01)
        sys.stdout.write("\r" + temp_str)
        sys.stdout.flush()
    sys.stdout.write("\n")
