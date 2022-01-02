import disnake
import os
import requests

from disnake import message
from disnake.ext import commands
from disnake.flags import Intents

description = '''The BloopyBoi, one of bloop.'''

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

bot.load_extension("cogs.inspire")
bot.load_extension("cog.blissfest")

bot.run(os.getenv('DISCORD_BOT_TOKEN'))
