#!/usr/bin/python3
""" LIFOCache module
"""
from typing import Union

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):   # type: ignore
    """ Class LIFOCache

        Attributes:
            - Inherits from BaseCaching
            - Discard last item in queue first
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize
            - Create superclass of init
            - Create array of keys
        """
        super().__init__()
        self.keys = []

    def put(self, key: str, item: str) -> None:
        """ Add an item in the cache using LIFO
        """
        if key or item:
            self.cache_data[key] = item

            self.keys.append(self.keys.pop(self.keys.index(key))) \
                if key in self.keys else self.keys.append(key)

            if len(self.keys) > BaseCaching.MAX_ITEMS:
                f = self.keys.pop(len(self.keys) - 2)
                del self.cache_data[f]
                print("DISCARD: {}".format(f))

    def get(self, key: str) -> Union[str, None]:
        """ Get an item by key using LIFO
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
