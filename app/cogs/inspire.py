
import disnake
from disnake.ext import commands
import requests


class InspireCommand(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot, inspiroBot_api_url):
        self.bot = bot
        self.api_url = inspiroBot_api_url
        self.backup_link = "https://generated.inspirobot.me/a/12PYMWaBPB.jpg"

    @commands.command()
    async def inspire(self, ctx: commands.Context):
        """Pull an image from inspiroBot allegedly"""
        inspiroBot_url = self.do_get_inspiro()
        msg = disnake.Embed()
        msg.set_image(url=inspiroBot_url)
        await ctx.send(embed=msg)

    def do_get_inspiro(self):
        """Do a GET to fetch link"""
        res = requests.get(self.api_url)
        if res.status_code == 200:
            return res.text
        else:
            return self.backup_link

def setup(bot: commands.Bot):
    api_url="https://inspirobot.me/api?generate=true"
    bot.add_cog(InspireCommand(bot, api_url))
