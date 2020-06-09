#!/usr/bin/env python3
""" Test suite for client
"""

from unittest import TestCase, mock
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from utils import requests


class TestGithubOrgClient(TestCase):
    """ Test cases for client.GithubOrgClient """
    @parameterized.expand([
        ("github", {"payload": True}),
        ("twitter", {"payload": True}),
        ("not a website", {"payload": False}),
    ])
    @patch('client.get_json')
    def test_org(self, name, payload, mock_get):
        """ test cases for client.org """
        instance = GithubOrgClient(name)
        mock_get.return_value = payload

        self.assertEqual(payload, instance.org)
        mock_get.assert_called_once()
