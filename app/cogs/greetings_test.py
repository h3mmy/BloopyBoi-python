"""Unit Tests For greetings Cog"""
import unittest
from disnake.ext import commands

from app.cogs.greetings import Greetings

class GreetingsTest(unittest.TestCase):
    """Unit Tests"""

    def setUp(self) -> None:
        test_bot = commands.Bot()
        self.test_cog = Greetings(bot=test_bot)

    def test_constructs_cog(self):
        """Unit Tests"""
        self.assertIsInstance(self.test_cog, commands.Cog)

if __name__ == '__main__':
    unittest.main()
