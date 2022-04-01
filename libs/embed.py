class Embed:
    def __init__(self, title=None, description=None, color=None, spoiler=False):
        self.title = title
        self.description = description
        self.color = color
        self.spoiler = spoiler
        self.field_data = None
        self.footer = None

    def add_field(self, name, value, inline=None):
        if not self.field_data:
            self.field_data = []
        self.field_data.append((name, value, inline))

    def set_footer(self, text):
        self.footer = text

    @property
    def create(self):
        content = ["||..." if self.spoiler else '...']
        content.extend([f"**{self.title}**", '---'])
        if self.description:
            content.append(f'{self.description}')
        if self.field_data:
            content.append('---')
            for data in self.field_data:
                if data[2]:
                    content[-1].join(f"`\t{data[0]}`: `{data[1]}`")
                else:
                    content.append(f"`{data[0]}`: `{data[1]}`")

        content.extend(["---||" if self.spoiler else '---'])

        if self.footer:
            content.append(f"_{self.footer}_")
        return "\n".join(content)
