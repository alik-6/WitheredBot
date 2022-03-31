from libs.embed import Embed
from .config import get


class EmbedHelp:
    def __init__(self, parent, accepted_args=None):
        self.parent = parent
        self.accepted_args = accepted_args
        self.prefix = get('PREFIX')

    def __call__(self):
        embed = Embed(
            title="Usage"
        )
        if self.accepted_args:
            description = f"{self.prefix}{self.parent.name}"
            for i in self.accepted_args:
                description += f" [{i}]"
                embed.description = description
            self.accepted_args = ', '.join(self.accepted_args)
            embed.add_field(name="Args", value=f"{self.accepted_args}")

        if self.parent.help:
            embed.add_field(name=f"Help", value=f"{self.parent.help}")
        if self.parent.aliases:
            embed.add_field(name="Aliases", value=f"{', '.join(self.parent.aliases)}")

        return embed.special

    def __repr__(self):
        print(f"({self.parent}, {self.accepted_args})")
