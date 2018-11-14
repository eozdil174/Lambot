import discord
import asyncio
import aiohttp
from discord.ext.commands import Bot
from discord import Game

TOKEN = "NTExOTY0NTEyODgzMTc5NTMw.DsykGg.4u9XqjdrgoinuI3r_kJRO_Dqm-E"

client = Bot(command_prefix="-")


images = {"bear":"tDbTPwI"}




@client.command(name="ping", description="Checks the bot's status",pass_context = True)
async def ping(ctx):
    await client.say("Pong :ping_pong:")

@client.command(name="post", description="Posts the image from imgur", pass_context = True)
async def post(ctx):
    name = ctx.message.content[6:]
    
    if name in images:
        await client.say("https://imgur.com/gallery/" + images[name])     
    else:
        await client.say("I don't have that image yet :(")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=Game(name="with memes"))

client.run(TOKEN)
