import logging
import os

import discord
import openai
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
openai.api_key = os.getenv('OPENAI_API_KEY')

intents = discord.Intents.default()
intents.message_content = True

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
bot = commands.Bot(
    command_prefix='$',
    intents=intents,
    log_handler=handler,
)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    synced = await bot.tree.sync()

@bot.tree.command(name='chatgpt', description='Prompt ChatGPT 3.5.')
async def chat(
        interaction: discord.Interaction,
        prompt: str,
        system_prompt: str | None = None,
        model: str = 'gpt-3.5-turbo',
        # messages: [{str: str}] = [],
        temperature: float = 1.0,
        top_p: int = 1,
        n: int = 1,
        max_tokens: int = 64,
        presence_penalty: float = 0.0,
        frequency_penalty: float = 0.0,
):
    if system_prompt:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ]
    else:
        messages = [{"role": "user", "content": prompt}]

    # TODO: Enable extended conversations and handle message history
    # if messages:
    #     messages.append({"role": "user", "content": prompt})
    # elif system_prompt:
    #     messages = [
    #         {"role": "system", "content": system_prompt},
    #         {"role": "user", "content": prompt},
    #     ]
    # else:
    #     messages = [{"role": "user", "content": prompt}]

    await interaction.response.defer()

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        n=n,
        max_tokens=max_tokens,
        presence_penalty=presence_penalty,
        frequency_penalty=frequency_penalty,
    )

    results = [x['message']['content'] for x in response.choices]

    msg = f'PARAMS: model={model}, temperature={temperature}, top_p={top_p}, n={n}, max_tokens={max_tokens}, presence_penalty={presence_penalty}, frequency_penalty={frequency_penalty}\n'
    msg += f'PROMPT: *{prompt}*\n\n'

    if len(results) > 1:
        for i, res in enumerate(results):
            msg += f'------------------------- v{i+1} -------------------------\n{res}\n\n'
    else:
        msg += results[0]

    await interaction.followup.send(msg)


bot.run(BOT_TOKEN)
