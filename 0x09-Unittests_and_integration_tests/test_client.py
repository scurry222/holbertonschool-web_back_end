#!/usr/bin/env python3
""" Test suite for client
"""

from unittest import TestCase, mock
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from utils import requests


class TestGithubOrgClient(TestCase):
    """ Test case for client.GithubOrgClient """
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False}),
    ])
    @patch('client.get_json')
    def test_org(self, name, payload, mock_get):
        """ test case for client.org """
        instance = GithubOrgClient(name)
        mock_get.return_value = payload

        self.assertEqual(payload, instance.org)
        mock_get.assert_called_once()

    def test_public_repos_url(self):
        """ test case for client._public_repos_url """
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_request:
            mock_request.return_value = {"url": 'http://scoutcurry.com'}

            res = GithubOrgClient(mock_request.return_value)._public_repos_url

            self.assertEqual(res, mock_request.return_value)
            mock_request.assert_called_once()


    @patch('client.get_json', return_value="test", new_callable=PropertyMock)
    def test_public_repos(self, mock_prop):
        """ test case for client._public_repos_url """
        mock_prop.return_value = GithubOrgClient("test")

        with patch('client.GithubOrgClient._public_repos_url',
                    return_value="test_repo") as mock_repo:
                mock_repo.return_value = GithubOrgClient("test_repo")
                res = GithubOrgClient("test_repo")._public_repos_url
                self.assertEqual(res, mock_repo.return_value)
        
        mock_prop.assert_called_once()