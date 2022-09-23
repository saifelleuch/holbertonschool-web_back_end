#!/usr/bin/python3
"""BasicCache that inherits from BaseCaching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class
    Args:
        BaseCaching ([class]): [BaseCaching module]
    """
    def put(self, key, item):
        """
        Must assign to the dictionary
        self.cache_data the item value for the key key.
        If key or item is None, this method should not do anything.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist
        in self.cache_data, return None.
        """
        return self.cache_data.get(key) or None
