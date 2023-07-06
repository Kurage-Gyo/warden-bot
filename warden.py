import discord
import os
import random
import asyncio
import re
from dotenv import load_dotenv

load_dotenv() #load dotenv variables
discord_token = os.getenv('DISCORD_TOKEN')
discord_guild = os.getenv('DISCORD_GUILD')
class MyClient(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)
    async def on_ready(self):
        print(f"Logged in as { self.user.name } (ID:{ self.user.id })")
        print(f"discord.py API version: { discord.__version__ }")
        print(f"------------------------------------------------")
        print(f"Setting {self.user.name}'s status to { 'do not disturb' }")
        await self.change_presence(status=discord.Status.dnd)
    async def on_message(self, message):
        if message.author.id == self.user.id: # we do not want the bot to reply to itself
            return
        if message.content.startswith('!hello'):
            await message.channel.send(f'Hello, {message.author.mention}. I, the {self.user.mention} bot says hi!')


intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

client = MyClient(intents=intents)
client.run(discord_token)