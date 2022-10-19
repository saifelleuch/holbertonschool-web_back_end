#!/usr/bin/env python3
"""
0x09. Unittests and Integration Tests
"""

from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """
    client.GithubOrgClient class
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """
        method should test that GithubOrgClient.org
        returns the correct value
        """
        test_class = GithubOrgClient(input)
        mock.side_effect = Exception()
        try:
            test_class.org()
        except Exception as e:
            mock.assert_called_once_with(
                f'https://api.github.com/orgs/{input}')

    def test_public_repos_url(self, org, expected):
        """
        test_public_repos_url method to unit-test
        GithubOrgClient._public_repos_url.
        """
        with patch('client.get_json') as mock:
            instance = GithubOrgClient(org)
            mock.return_value = expected
            self.assertEqual(instance._public_repos_url, expected["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        TestGithubOrgClient.test_public_repos to
        unit-test GithubOrgClient.public_repos.
        """

        Response_payload = [{"name": "Google"}]
        mock_json.return_value = Response_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [rep["name"] for rep in Response_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()
    p = [({"license": {"key": "my_license"}}, "my_license", True),
         ({"license": {"key": "other_license"}}, "my_license", False)]

    @parameterized.expand(p)
    def test_has_license(self, mapping, license_key, excepted):
        """
        TestGithubOrgClient.test_has_license
        to unit-test GithubOrgClient.has_license.
        """

        self.assertEqual(GithubOrgClient.has_license(
            mapping, license_key), excepted)
