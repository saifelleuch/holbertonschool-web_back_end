#!/usr/bin/python3
"""class MRUCache that inherits from BaseCaching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """class MRUCache that inherits from BaseCaching
    """
    def __init__(self):
        super().__init__()
        self.current_cache = []

    def put(self, key, item):
        """Must assign to the dictionary
        self.cache_data the item value for the key key
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.current_cache:
                self.current_cache.append(key)
            else:
                self.current_cache.append(
                    self.current_cache.pop(self.current_cache.index(key)))
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                key_discarded = self.current_cache.pop(-2)
                del self.cache_data[key_discarded]
                print("DISCARD: {}".format(key_discarded))

    def get(self, key):
        """Must return the value in
        self.cache_data linked to key.
        """
        if key and key in self.cache_data:
            self.current_cache.append(
                self.current_cache.pop(self.current_cache.index(key)))
            return self.cache_data.get(key)
        return None
