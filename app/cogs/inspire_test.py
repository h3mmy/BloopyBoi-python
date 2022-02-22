"""Unit Tests for Inspire Cog"""
import unittest
from unittest import mock
from disnake.ext import commands

from . import inspire

MOCK_API_URL="http://api.url/mock.json"
MOCK_RETURN_LINK="http://mock_link"

def mocked_requests_get(*args):
    """This method will be used by the mock to replace requests.get"""
    class MockResponse:
        """MockResponse Object"""
        def __init__(self, string_data, status_code):
            """Creates MockResponse"""
            self.string_data = string_data
            self.status_code = status_code
            self.text = self.string_data

        def status(self):
            """Returns Status Code"""
            return self.status_code

    if args[0] == MOCK_API_URL:
        return MockResponse(MOCK_RETURN_LINK, 200)

    return MockResponse(None, 404)

class InspireCommandTest(unittest.TestCase):
    """Unit Tests"""

    def setUp(self) -> None:
        test_bot = commands.Bot()
        self.test_cog = inspire.InspireCommand(test_bot, MOCK_API_URL)

    def test_constructs_cog(self):
        """Unit Tests"""
        self.assertIsInstance(self.test_cog, commands.Cog)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_do_get_inspiro(self, mock_get):
        """Test for do_get_inspiro(api_url)"""
        res = inspire.do_get_inspiro(MOCK_API_URL)
        self.assertEqual(res,MOCK_RETURN_LINK)
        self.assertIn(mock.call(MOCK_API_URL), mock_get.call_args_list)

        res_fail = inspire.do_get_inspiro("http://bad.url")
        self.assertEqual(res_fail, inspire.BACKUP_LINK)

if __name__ == '__main__':
    unittest.main()
