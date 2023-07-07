import discord
import os
import random
import asyncio
import re
from discord import app_commands
from dotenv import load_dotenv


load_dotenv() #load dotenv variables
discord_token = os.getenv('DISCORD_TOKEN')
discord_guild = discord.Object(os.getenv('DISCORD_GUILD')) #get variable, set the id as discord.Object
class MyClient(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self) #init command tree
    async def setup_hook(self): 
        # This copies the global commands over to specified guild.
        self.tree.copy_global_to(guild=discord_guild)
        await self.tree.sync(guild=discord_guild)
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

@client.tree.command()
@app_commands.describe(message='The message you want me to repeat')
async def say(interaction: discord.Interaction, message: str):
    """Repeats what you say"""
    await interaction.response.send_message(f'*{message}*') #Repeats given message 


client.run(discord_token)