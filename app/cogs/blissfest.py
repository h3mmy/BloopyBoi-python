"""Module docstring"""
import disnake
from disnake.ext import commands


class BlissfestCommand(commands.Cog):
    """This will be for the blissfest command."""

    def __init__(self, bot: commands.Bot, blissfest_excite_url):
        self.bot = bot
        self.excite_url = blissfest_excite_url

    @commands.command()
    async def blissfest(self, ctx: commands.Context):
        """Pull an image from inspiroBot allegedly"""
        blissfest_excite_url = self.excite_url
        msg = disnake.Embed()
        msg.set_image(url=blissfest_excite_url)
        await ctx.send(embed=msg)

def setup(bot: commands.Bot):
    """Sets up Cog"""
    api_url="https://github.com/h3mmy/BloopyBoi/raw/main/app/assets/blissfest_1.gif"
    bot.add_cog(BlissfestCommand(bot, api_url))
