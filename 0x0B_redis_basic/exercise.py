#!/usr/bin/env python3
""" 0x0B. Redis basic """

from typing import Union, Optional, Callable
import redis
import uuid


class Cache:
    """ Cache class """
    def __init__(self):
        """ initialization of Cache class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @store
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ method that takes a data argument and returns a string """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """take a key string argument and an optional Callable
        argument named fn. This callable will be used to
        convert the data back to the desired format."""
        data = self._redis.get(key)
        if key is none:
            return fn(data)

    def get_str(self, key: str) -> str:
        """automatically parametrize Cache.get with
        the correct conversion function."""
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """automatically parametrize Cache.get with
        the correct conversion function."""
        data = self._redis.get(key)
        try:
            data = int(value.decode("utf-8"))
        except Exception:
            data = 0
        return data
