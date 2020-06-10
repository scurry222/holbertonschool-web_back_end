#!/usr/bin/env python3
""" Test suite for client
"""

from unittest import TestCase, mock
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from utils import requests


class TestGithubOrgClient(TestCase):
    """ Test cases for client.GithubOrgClient """
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False}),
    ])
    @patch('client.get_json')
    def test_org(self, name, payload, mock_get):
        """ test cases for client.org """
        instance = GithubOrgClient(name)
        mock_get.return_value = payload

        self.assertEqual(payload, instance.org)
        mock_get.assert_called_once()

    def test_public_repos_url(self):
        """ test cases for client._test_public_repos_url """
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_request:
            mock_request.return_value = {"url": 'http://scoutcurry.com'}

            res = GithubOrgClient(mock_request.return_value)._public_repos_url

            self.assertEqual(res, mock_request.return_value)
            mock_request.assert_called_once()
