import discord
import os 
from chesscom_funcs import *

BOT_TOKEN = os.environ.get("BOT_TOKEN")

client = discord.Client()

@client.event
async def on_event():
    print("Bot ready! Signed in as ", client.user)

@client.event
async def on_message(message):
    if message.author == client.user:
        print("Message ignored, author is bot.")
        return
    
    if message.content.startswith("!hello"):
        await message.channel.send("Hello")

    if message.content.startswith("!update-rating"):
        account = message.content.lstrip("!update-rating")

client.run(BOT_TOKEN)
