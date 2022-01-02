import disnake
import os
import requests

from disnake import message
from disnake.ext import commands
from disnake.flags import Intents

description = '''The BloopyBoi, one of bloop.'''
blissfest_1 = "https://github.com/h3mmy/BloopyBoi/raw/main/app/assets/blissfest_1.gif"

intents = disnake.Intents.default()

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

@bot.event
async def on_ready():
    """Announces self to std.out"""
    print('We have logged in as {0} {1}'.format(bot.user.name, bot.user.id))

@bot.command()
async def hello(ctx):
    """Says hello, prints ctx maybe"""
    if ctx:
        await ctx.send('Hello to you as well humanoid! This is an experiment. I will be upto mischief in no time')

@bot.command()
async def blissfest(ctx):
    """Hypes Blissfest"""
    blissfest_excite_url=blissfest_1
    msg = disnake.Embed()
    msg.set_image(url=blissfest_excite_url)
    await ctx.send(embed=msg)

bot.load_extension("cogs.inspire")

bot.run(os.getenv('DISCORD_BOT_TOKEN'))
