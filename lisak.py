import discord
import os
import dotenv
import logging


dotenv.load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run(os.getenv('TOKEN'), log_handler=handler)