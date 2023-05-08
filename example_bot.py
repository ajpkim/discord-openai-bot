import logging
import os

import discord
import openai
from discord.ext import commands

from dotenv import load_dotenv

from functools import reduce
from operator import mul

load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
openai.api_key = os.getenv('OPENAI_API_KEY')

intents = discord.Intents.default()
intents.message_content = True

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
bot = commands.Bot(command_prefix='$', intents=intents, log_handler=handler)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    synced = await bot.tree.sync()
    print('Slash commands synced:', len(synced))

@bot.tree.command(name='add', description='Sum the given numbers.')
async def add(interaction: discord.Interaction, n1: float, n2: float):
    """Sum the given numbers."""
    # await interaction.response.send_message(content='Checking the numbers...')
    res = n1 + n2
    await interaction.response.send_message(res)

@bot.tree.command(name='divide', description='Divide the given numbers.')
async def divide(interaction: discord.Interaction, n1: float, n2: float):
    """Sum the given numbers."""
    # await interaction.response.send_message(content='Checking the numbers...')
    res = n1 / n2
    await interaction.response.send_message(res)

bot.run(BOT_TOKEN)
