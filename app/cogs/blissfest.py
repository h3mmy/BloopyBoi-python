"""Module docstring"""
from datetime import date
import disnake
from disnake.ext import commands

BLISSFEST_DATE = date(2022,7,8)

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

    @commands.command()
    async def bliss(self, ctx: commands.Context):
        """Returns days left to BLISSFEST_DATE"""
        days_left = BLISSFEST_DATE-date.today()
        msg = self.build_countdown_msg(days_left)
        await ctx.send(embed=msg)

    def new_method(self, days_left):
        """Builds the embedded countdown message"""
        return disnake.Embed(
            title="🏕 Blissfest! 🎶🎼",
            description=f"Only {days_left.days} Days Left!")

    @commands.slash_command()
    async def blissme(self, inter: disnake.CommandInteraction, user: disnake.User):
        await inter.response.send_message(f"Goddess Bliss You {user.display_name}")


def setup(bot: commands.Bot):
    """Sets up Cog"""
    api_url="https://github.com/h3mmy/BloopyBoi/raw/main/app/assets/blissfest_1.gif"
    bot.add_cog(BlissfestCommand(bot, api_url))
