import discord
import os
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
        print(f"Setting {self.user.name}'s status to { 'do not disturb','r' }")
        await self.change_presence(status=discord.Status.dnd)

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

client = MyClient(intents=intents)
client.run(discord_token)