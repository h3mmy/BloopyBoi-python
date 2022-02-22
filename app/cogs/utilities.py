"""Module docstring"""
import disnake
from disnake.ext import commands
import requests

class UtilityCommand(commands.Cog):
    """This will be for various utility commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def wink(self, inter):
        """Does a wink"""
        # pylint   disable=no-self-use
        await inter.response.send_message("winked")

    @commands.command()
    @commands.is_owner()
    async def check(self, ctx: commands.Context):
        """Check Status"""
        # pylint   disable=no-self-use
        is_alive = check_liveness(f"https://{ctx.args[0]}")
        msg = disnake.Embed()
        msg.color="green" if is_alive else "red"
        msg.description=f"{ctx.args[0]} is alive-ish?"
        await ctx.send(embed=msg)

def check_liveness(url):
    """Checks for 200 codes"""
    return requests.get(url).status_code in [200, 201]

def setup(bot: commands.Bot):
    """Sets up Cog"""
    bot.add_cog(UtilityCommand(bot))
