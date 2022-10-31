#!/usr/bin/env python3
""" 0x0B. Redis basic """

from ctypes import Union
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
