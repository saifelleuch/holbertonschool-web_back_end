#!/usr/bin/env python3
"""
0x09. Unittests and Integration Tests
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from unittest.mock import patch
from unittest.mock import MagicMock


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class
    that inherits from unittest.TestCase.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",))
        ({"a": {"b": 2}}, ("a",))
        ({"a": {"b": 2}}, ("a", "b"))
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> bool:
        """
        method to test that the method
        returns what it is supposed to
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a"))
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        TestAccessNestedMap.test_access_nested_map_exception
        """
        with self.assertRaises(KeyError) as raises:
            access_nested_map(nested_map, path)
            self.assertEqual(raises.exception.message, KeyError)

class TestGetJson(unittest.TestCase):
    """
    TestGetJson(unittest.TestCase) class 
    """

    @parameterized.expand([("http://example.com", {"payload": True})
                           ("http://holberton.io", {"payload": False})
                        ])
    def test_get_json(self, url, payload, expected):
        """
        method to test that utils.get_json
        returns the expected result.
        """
        with patch('utils.requests') as mock_requests:
            mock_requests.get.return_value = self.response(payload)
            self.assertEqual(get_json(url), expected)
            assert mock_requests.get.call_count == 1

class TestMemoize(unittest.TestCase):
    """
    TestMemoize(unittest.TestCase) class 
    """

    def test_memoize(self):
        """
        test_memoize method.
        """
        class TestClass:
            """
            TestClass
            """

            def a_method(self):
                """
                a_method
                """
                return 42

            @memoize
            def a_property(self):
                """
                a_property
                """
                return self.a_method()

        c = TestClass()
        c.a_method = MagicMock(return_value=42)
        self.assertEqual(c.a_property, 42)
        self.assertEqual(c.a_property, 42)
        c.a_method.assert_called_once()
