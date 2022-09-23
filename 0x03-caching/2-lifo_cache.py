#!/usr/bin/python3
""" LIFOCache that inherits from BaseCaching """
BasicCaching = __import__('base_caching').BaseCaching


class LIFOCache(BasicCaching):
    """LIFOCache that inherits from BaseCaching"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data
        the item value for the key key.
        """
        len_stored_cache = len(self.cache_data)
        if key and item:
            if len_stored_cache >= BasicCaching.MAX_ITEMS and str(
                    key) not in self.cache_data:
                key_discarded = list(self.cache_data.keys())
                [len_stored_cache - 1]
                print("DISCARD: {}".format(key_discarded))
                self.cache_data.pop(key_discarded)
            self.cache_data[str(key)] = item

    def get(self, key):
        """Must return the value in
        self.cache_data linked to key."""
        if key:
            return self.cache_data.get(key)
        else:
            return None
