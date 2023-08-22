import discord
from discord.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import youtube_dl

bot_intents = discord.Intents.default()
bot_intents.members = True
bot_intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=bot_intents)

client_id = "YOUR_CLIENT_ID_HERE"
client_secret = "YOUR_CLIENT_SECRET_HERE"

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret
    ))
ytdl = youtube_dl.YoutubeDL({'format': 'bestaudio', 'noplaylist': 'True'})

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@bot.command()
async def play(ctx, url):
    ctx.voice_client.stop()

    # Перевіряємо, чи URL від YouTube чи Spotify
    if "youtube.com/watch?v=" in url:
        info = ytdl.extract_info(url, download=False)
        url = info['formats'][0]['url']
        title = info['title']
    else:
        track_info = sp.track(url)
        preview_url = track_info['preview_url']
        url = preview_url
        title = track_info['name']

    player = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url))
    ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
    await ctx.send(f"Now playing: {title}")

bot.run('YOUR_BOT_TOKEN_HERE')

рпрпм

