#!/usr/bin/env python3
""" Test suite for utils
"""

from unittest import TestCase, mock
from parameterized import parameterized
from utils import requests, get_json, access_nested_map, memoize


class TestAccessNestedMap(TestCase):
    """ Test cases for utils.test_access_nested_map """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, values, path, expected):
        """ Test utils.test_access_nested_map """
        ret = access_nested_map(values, path)
        self.assertEqual(ret, expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, values, path, expected):
        """ Test utils.test_access_nested_map exception """
        with self.assertRaises(KeyError) as e:
            access_nested_map(values, path)
            self.assertEqual(expected, str(e.exception))


class TestGetJson(TestCase):
    """ Test cases for utils.get_json """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test utils.get_json """

        res = mock.Mock()
        res.json.return_value = test_payload

        with mock.patch('requests.get', return_value=res):
            mock_request = get_json(test_url)
            res.json.assert_called_once()
            self.assertEqual(mock_request, test_payload)


class TestMemoize(TestCase):
    """ Test cases for utils.memoize """

    def test_memoize(self):
        """ Test utils.memoize """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method') as mock_object:
            """ test a_method """
            instance = TestClass()
            instance.a_property()
            instance.a_property()
            mock_object.assert_called_once()


if "__name__" == "__main__":
    unittest.main()
