# This example requires the 'message_content' intent.

import logging
import os

import discord
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Don't respond to our own messages
    if message.author == client.user:
        return

    if message.content.startswith('$Yo'):
        await message.channel.send('Hello friend!')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
client.run(BOT_TOKEN, log_handler=handler)
