#!/usr/bin/python3
"""
class LFUCache that inherits from BaseCaching
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    class LFUCache that inherits from BaseCaching
    """

    def __init__(self):
        self.usedKey = {}
        self.timesKey = {}
        self.time = 0
        super().__init__()

    def put(self, key, item):
        """
        Must assign to the dictionary
        self.cache_data the item value for the key key.
        """
        if key is not None and item is not None:
            if key not in self.usedKey:
                self.usedKey[key] = 1
            else:
                self.usedKey[key] += 1
            self.timesKey[key] = self.time
            self.time += 1
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            cpyusedKey = self.usedKey.copy()
            del cpyusedKey[key]
            the_smallest_value = min(cpyusedKey, key=cpyusedKey.get)
            the_smallest_value = cpyusedKey[the_smallest_value]
            sameKeyValue = {}
            for _key, _value in cpyusedKey.items():
                if _value == the_smallest_value:
                    sameKeyValue[_key] = _value
            if len(sameKeyValue) == 1:
                key_discarded = list(sameKeyValue.keys())[0]
            else:
                time_sameKeyValue = {}
                for _key, _value in self.timesKey.items():
                    if _key in sameKeyValue:
                        time_sameKeyValue[_key] = _value

                key_discarded = min(time_sameKeyValue, key=time_sameKeyValue.get)
            del self.cache_data[key_discarded]
            del self.usedKey[key_discarded]
            del self.timesKey[key_discarded]

            print("DISCARD: {}".format(key_discarded))

    def get(self, key):
        """
        Must return the value in
        self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        self.usedKey[key] += 1
        self.timesKey[key] = self.time
        self.time += 1
        return self.cache_data[key]