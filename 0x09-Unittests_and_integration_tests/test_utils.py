#!/usr/bin/env python3
"""
0x09. Unittests and Integration Tests
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import Mapping, Sequence, Any


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
