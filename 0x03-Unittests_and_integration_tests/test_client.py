import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        # Set up a mock return value for get_json
        mock_get_json.return_value = {"login": org_name}

        # Create an instance of GithubOrgClient and call the org method
        client = GithubOrgClient(org_name)
        result = client.org

        # Verify that get_json was called with the correct URL
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        # Check that the org method returns the expected result
        self.assertEqual(result, {"login": org_name})
