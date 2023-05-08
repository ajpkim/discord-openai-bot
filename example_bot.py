import logging
import os

import discord
import openai
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
openai.api_key = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
bot = commands.Bot(command_prefix='$', intents=intents, log_handler=handler)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    synced = await bot.tree.sync()
    print('Slash commands synced:', len(synced))

@bot.command()
async def add(ctx, *args):
    """Adds given numbers."""
    res = sum(map(float, args))
    await ctx.send(res)

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


bot.run(BOT_TOKEN)
