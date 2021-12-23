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
