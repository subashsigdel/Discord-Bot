import discord
from discord.ext import commands
import yt_dlp
import asyncio
import os

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

FFMPEG_OPTIONS = {'options': '-vn'}
YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': True}

class MusicBot(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.queue = []

    @commands.command()
    async def bajau(self, ctx, *, search):
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None
        if not voice_channel:
            return await ctx.send("voice channel ma ja paila ")

        if not ctx.voice_client:
            await voice_channel.connect()

        async with ctx.typing():
            with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(f'ytsearch:{search}', download=False)
                if 'entries' in info:
                    info = info['entries'][0]
                url = info['url']
                title = info['title']
                self.queue.append((url, title))
                await ctx.send(f'ok sir: **{title}**')
        if not ctx.voice_client.is_playing():
            await self.play_next(ctx)

    async def play_next(self, ctx):
        if self.queue:
            url, title = self.queue.pop(0)
            source = await discord.FFmpegOpusAudio.from_probe(url, **FFMPEG_OPTIONS)
            ctx.voice_client.play(source, after=lambda _: self.client.loop.create_task(self.play_next(ctx)))
            await ctx.send(f'la suna **{title}**')
        elif not ctx.voice_client.is_playing():
            await ctx.send('geet xaina !!!')

    @commands.command()
    async def arko(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            await ctx.send("Skipped")

client = commands.Bot(command_prefix="geet ", intents=intents)

async def main():
    token = os.getenv('DISCORD_SECRET_TOKEN2')
    print(f'Token: {token}')  # Add this line for debugging
    if token is None:
        raise ValueError("DISCORD_SECRET_TOKEN2 environment variable is not set")
    await client.add_cog(MusicBot(client))
    await client.start(token)

asyncio.run(main())
