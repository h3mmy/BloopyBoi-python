"""Module docstring"""
import disnake
from disnake.ext import commands
import requests

BACKUP_LINK="https://generated.inspirobot.me/a/12PYMWaBPB.jpg"

class InspireCommand(commands.Cog):
    """This will be for the inspire command."""

    def __init__(self, bot: commands.Bot, inspirobot_api_url):
        self.bot = bot
        self.api_url = inspirobot_api_url

    @commands.command()
    async def inspire(self, ctx: commands.Context):
        """Pull an image from inspiroBot allegedly"""
        inspirobot_url = do_get_inspiro(self.api_url)
        msg = disnake.Embed()
        msg.set_image(url=inspirobot_url)
        await ctx.send(embed=msg)

def do_get_inspiro(api_url):
    """Do a GET to fetch link"""
    res = requests.get(api_url)
    if res.status_code == 200:
        return res.text()
    return BACKUP_LINK

def setup(bot: commands.Bot):
    """Sets up Cog"""
    api_url="https://inspirobot.me/api?generate=true"
    bot.add_cog(InspireCommand(bot, api_url))
