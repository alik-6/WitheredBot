from distutils import command
from pydoc import describe
from discord.ext import commands
from discord import Embed
from libs.help import EmbedHelp
from libs.extras import to_discord_str
from asyncio import sleep 
import sqlite3
from libs.config import DATABASE_NAME

class Extras:
    def check(self):
        connection = sqlite3.connect(DATABASE_NAME)
        conn = connection.cursor()
        conn.execute("""
        CREATE TABLE IF NOT EXISTS Saves (
            key TEXT NOT NULL UNIQUE,
            value TEXT
        );
        """)
        connection.commit()
        connection.close()

    def set(self, key:str, value: str):
        self.check()
        connection = sqlite3.connect(DATABASE_NAME)
        conn = connection.cursor()
        try:
            conn.execute("INSERT INTO Saves(key, value) VALUES(? , ?);", (key, value,))
            connection.commit()
            connection.close()
            return {'Added': 'Key Added'}
        except sqlite3.IntegrityError:
            return {'Error': 'It Already Exists'}


    def get(self, key: str) ->dict:
        self.check()
        connection = sqlite3.connect(DATABASE_NAME)
        conn = connection.cursor()
        value = conn.execute("SELECT * FROM Saves where key = ?;", (key,)).fetchone()
        connection.commit()
        connection.close()
        if value:
            return {'Sucess': value}
        else:
            return {'Error': 'It\'s Not There'}
        
    def get_all(self) -> dict:
        self.check()
        connection = sqlite3.connect(DATABASE_NAME)
        conn = connection.cursor()
        value = conn.execute("SELECT * FROM Saves;").fetchall()
        connection.commit()
        connection.close()
        if value:
            return {'Sucess': value}
        else:
            return {'Error': 'It\'s Not There'}
    def delete(self, key: str):
        self.check()
        connection = sqlite3.connect(DATABASE_NAME)
        conn = connection.cursor()
        conn.execute("DELETE FROM Saves WHERE key = ?",(key,))
        connection.commit()
        connection.close()

class Init(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.store = Extras()

    @commands.command()
    async def save(self, ctx, title=None, content=None):
        if not title or not content:
            help = EmbedHelp(self.save, accepted_args=["title", "content"])
            await ctx.send(embed=await(help()))
        
        else:
            data = self.store.set(key=title, value=content)
            if data.get('Added'):
                await ctx.send(embed=Embed(
                    title="Added!!",
                    description=data.get("Added")
                ))
            else:
                await ctx.send(embed=Embed(
                    title="Error!!",
                    description=data.get("Error")
                ))
        
    @commands.command()
    async def get(self, ctx, key=None):
        if not key:
            help = EmbedHelp(self.get, accepted_args=["title"])
            await ctx.send(embed=await(help()))

        else:
            key = str(key)
            data = self.store.get(key)
            if data.get('Sucess'):
                data =data.get('Sucess')
                await ctx.send(embed=Embed(
                    title=data[0],
                    description=data[1]
                ))
            else:
                await ctx.send(embed=Embed(
                    title="Error!!",
                    description=data.get("Error")
                ))

    @commands.command()
    async def delete(self, ctx, key=None):
        if not key:
            help = EmbedHelp(self.delete, accepted_args=["title"])
            await ctx.send(embed=await(help()))
        else:
            key = str(key)
            data = self.store.get(key)
            if data.get('Sucess'):
                self.store.delete(key)
                await ctx.send(embed=Embed(
                    title="Deleted",
                    description="Key Removed"
                ))
            else:
                await ctx.send(embed=Embed(
                    title="Error!!",
                    description=data.get("Error")
                ))
    @commands.command()
    async def list(self,ctx):
       
        data = self.store.get_all()
        if data.get('Sucess'):
            data =data.get('Sucess')
            embed=Embed(
                title="List",
                description="All Enteries"
            )
            list_data = "[C]"
            for i in data:
                list_data += f"¬ {i[0]}\n"
            list_data += '[C]'
            embed.add_field(name='Entries', value=to_discord_str(list_data))
            await ctx.send(embed=embed)
        else:
            await ctx.send(embed=Embed(
                title="Error!!",
                description=data.get("Error")
            ))


def setup(bot) -> dict:
    return {
        "Object": Init(bot),
        "name": "Savey",
        "description": "Leave Remembering to me :wink:",
    }
