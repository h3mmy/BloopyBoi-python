"""Unit Tests"""
import unittest
from disnake.ext import commands

from app.cogs import BlissfestCommand


class BlissfestCommandTest(unittest.TestCase):
    """Unit Tests"""

    def setUp(self) -> None:
        test_bot = commands.Bot()
        self.test_cog = BlissfestCommand(bot=test_bot)

    def test_constructs_cog(self):
        """Unit Tests"""
        self.assertIsInstance(self.test_cog, commands.Cog)

if __name__ == '__main__':
    unittest.main()
