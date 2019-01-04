import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is Ready!")

@client.event
async def on_message(message):
    if message.author.id == "Overlord Pete#9313":
        await client.send_message(message.channel, "I live to sate your bloodlust, Father")
    if message.author == "Pete":
        await client.send_message(message.channel, "I live to sate your bloodlust, Father")
    if message.content.upper().__contains__("COOKIE"):
        if message.content.upper().__contains__(":COOKIE:"):
            pass
        else:
            await client.send_message(message.channel, ":cookie:") #responds with Cookie emoji when someone says "cookie"
    if message.content.upper().startswith("SIC"):
        await client.send_message(message.channel, "I live to sate your bloodlust, Father") #responds with Cookie emoji when someone says "cookie"
    if message.content.upper().__contains__("RWBY"):
        await client.send_message(message.channel, "<:Chibi:530868533211561985>")
    if message.content.upper().__contains__("RUBY"):
        await client.send_message(message.channel, "<:Chibi:530868533211561985>")



client.run("NTI3OTYyNjAwMjMxNzk2NzM5.DwbY0A.PVhu9zH5DrW976GpopEJQtmmBJI")