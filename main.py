# all library
import discord
import os
import time

from dotenv import load_dotenv
from discord.ext import commands

# ai
from ai import request

load_dotenv()

# env data
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# visual
print("Starting BOT...")
time.sleep(1.5)

# connect to the bot
BOT_DISCORD = commands.Bot(
    command_prefix="!",
    intents=discord.Intents.default()
)

# register command
@BOT_DISCORD.tree.command(name="ask", description="Ask something to the AI")
async def ask(interaction: discord.Interaction, prompt: str):
    reply = request(prompt)
    await interaction.response.send_message(reply)

# cek bot
@BOT_DISCORD.event
async def on_ready():
    print("Successful connect to the bot as", BOT_DISCORD.user)
    await BOT_DISCORD.tree.sync()
    print("Successfully sync commands!")

# run bot
if not DISCORD_TOKEN:
    print("[ERROR] DISCORD_TOKEN not found!")
    exit(1)

BOT_DISCORD.run(DISCORD_TOKEN)
