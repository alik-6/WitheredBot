from discord.ext import (commands)
from libs.help import EmbedHelp
from libs.config import get
from discord import (Embed)
import requests
from base64 import b64encode
from discord import Colour

class Extras:
    def get_token(self):
        SECRET = get('SPOTIFY_CLIENT_SECRET')
        ID = get('SPOTIFY_CLIENT_ID') 
        if ID and SECRET:
            client_creds = b64encode(f"{ID}:{SECRET}".encode())
            url = "https://accounts.spotify.com/api/token"
            DATA = {
                'grant_type': 'client_credentials'
            }
            HEADERS = {
                'Authorization': f"Basic {client_creds.decode()}"
            }

            req = requests.post(url, data=DATA, headers=HEADERS)
            token = req.json().get('access_token')
            if token:
                return token
            else:
                return None
        else:
            return None

    def process_song_data(self, req):
        req = req['tracks']['items']
        if req == []:
            return None
        else:
            album = req[0]['album']
            artists = []
            for artist in album['artists']:
                artists.append(artist['name'])

            data = {
                "artists": ", ".join(artists),
                "name": req[0]['name'],
                "date": album['release_date'],
                "time": round(req[0]['duration_ms']/1000/60)       ,
                "url": req[0]['external_urls']['spotify'],
                "image": album['images'][1]["url"]
            }
            return data

    def get_song_data(self, term, token):
        PARAMS = {"q": term, "type": "track", "market": "ES", "limit": 1}

        HEADERS = {
                "Authorization": f"""Bearer {token}"""
        }
        req = requests.get("https://api.spotify.com/v1/search", params=PARAMS, headers=HEADERS)

        return req.json()

class Init(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.extras = Extras()
        self.color = Colour.green()

    

    @commands.command()
    async def spotify(self, ctx, *term):
        "Search the Spotify "
        term = " ".join(term)
        token = self.extras.get_token()
        if not token:
            await ctx.send(embed=Embed(title="Spotify", description="Invalid Credentials", color=self.color))
        if term.strip() == "":
            help = EmbedHelp(self.spotify, accepted_args=['songname'])
            await ctx.send(embed=await(help()))

        else:
            song_data = self.extras.process_song_data(self.extras.get_song_data(term, token))
            if song_data:
                e = Embed(title=song_data.get('name'), description=f"By {song_data.get('artists')}", url=song_data.get('url'), color=self.color)
                e.add_field(name="Duration", value=f"`{song_data.get('time')}mins`", inline=False)
                e.set_footer(text=f"Published on {song_data.get('date')}")
                e.set_image(url=song_data.get('image'))
                await ctx.send(embed=e)
            else:
                await ctx.send(embed=Embed(
                    title="Spotify",
                    description="No Songs Found", 
                    color=self.color
                ))

def setup(bot) -> dict:
    return {
        "Object": Init(bot),
        "name": "Spotify",
        "description": "Search for Songs on Spotify",
        "required_keys": ["SPOTIFY_CLIENT_SECRET", "SPOTIFY_CLIENT_ID"],
    }
