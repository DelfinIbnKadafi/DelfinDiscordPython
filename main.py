# all library
import discord
import os
import time

from dotenv import load_dotenv

load_dotenv()

# env data
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# visual
print("Starting BOT...")
time.sleep(1.5)

# connect to the bot
BOT_DISCORD = discord.Client(intents=discord.Intents.default())

# cek bot
@BOT_DISCORD.event
async def on_ready():
    print("Succesfull connect to the bot as", BOT_DISCORD.user)

BOT_DISCORD.run(DISCORD_TOKEN)
