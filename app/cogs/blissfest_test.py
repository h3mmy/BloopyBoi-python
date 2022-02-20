"""Unit Tests For Blissfest Cog"""
import unittest
from disnake.ext import commands

import blissfest           # pylint: disable=import-error

class BlissfestCommandTest(unittest.TestCase):
    """Unit Tests"""

    def setUp(self) -> None:
        test_bot = commands.Bot()
        self.test_cog = blissfest.BlissfestCommand(bot=test_bot, blissfest_excite_url="test_url")

    def test_constructs_cog(self):
        """Unit Tests"""
        self.assertIsInstance(self.test_cog, commands.Cog)

if __name__ == '__main__':
    unittest.main()
