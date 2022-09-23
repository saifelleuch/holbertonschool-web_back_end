#!/usr/bin/python3
"""
FIFOCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache that inherits from
    BaseCaching and is a caching system
    """
    def __init__(self):
        """
        init
        """
        super().__init__()
        self.current_cache = []

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data
        the item value for the key key.
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.current_cache:
                self.current_cache.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.current_cache.pop(0)
                del self.cache_data[discarded]
                print("DISCARD: {}".format(discarded))

    def get(self, key):
        """Must return the value in
        self.cache_data linked to key
        """
        return self.cache_data.get(key) or None
