import discord
import os
import requests

from discord import message
from discord.ext import commands
from discord.flags import Intents

description = '''The BloopyBoi, one of bloop.'''
inspiroBot_api_url="https://inspirobot.me/api?generate=true"
backup_link = "https://generated.inspirobot.me/a/12PYMWaBPB.jpg"

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

@bot.event
async def on_ready():
    """Announces self to std.out"""
    print('We have logged in as {0} {1}'.format(bot.user.name, bot.user.id))

@bot.command()
async def hello(ctx):
    """Says hello, prints ctx maybe"""
    if ctx:
        await ctx.send('Hello to you as well humanoid! This is an experiment. The context is {0}'.format(ctx))

@bot.command()
async def inspire(ctx):
    """Pull an image from inspiroBot allegedly"""
    inspiroBot_url = do_get_inspiro()
    msg = discord.Embed()
    msg.set_image(url=inspiroBot_url)
    await ctx.send(embed=msg)

def do_get_inspiro():
    """Do a GET to fetch link"""
    res = requests.get(inspiroBot_api_url)
    print(res.text)
    if res.status_code == 200:
        return res.text
    else:
        return backup_link


bot.run(os.getenv('DISCORD_BOT_TOKEN'))
