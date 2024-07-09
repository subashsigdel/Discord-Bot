import os
import discord
from discord.ext import commands

# Read the secret token from the environment variable
DISCORD_SECRET_TOKEN = os.getenv('DISCORD_SECRET_TOKEN')

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
intents.message_content = True  # Add this line to enable message content intent

# Create bot instance with command prefix '!'
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: on_ready
@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

# Command: mention
@bot.command()
async def gali0(ctx, member: discord.Member):
        if member.display_name.lower() == 'rasenga' or member.name.lower() == 'rasenga':
            await ctx.send(f'{member.mention},Lord rasenga is our Master you idiot. we cant do it')
        else:
            await ctx.send(f'{member.mention}, You Blithering Idiot')

# Command: mention
@bot.command()
async def gali1(ctx, member: discord.Member):
        await ctx.send(f'{member.mention}, You Fucking Moron')

# Command: mention
@bot.command()
async def gali2(ctx, member: discord.Member):
        await ctx.send(f'{member.mention}, you fucking pain in the ass')

# Command: mention
@bot.command()
async def gali3(ctx, member: discord.Member):
        await ctx.send(f'{member.mention},you shitty head')

# Command: mention
@bot.command()
async def gali4(ctx, member: discord.Member):
        await ctx.send(f'{member.mention}, Holy Mary Mother of Jesus what is that')

# Run the bot with your token
bot.run(DISCORD_SECRET_TOKEN)
