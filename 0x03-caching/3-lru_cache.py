#!/usr/bin/python3
""" LRUCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Class LRUCache

        Attributes:
            - Inherits from BaseCaching
            - Discard least recently used items first
    """

    def __init__(self):
        """ Initialize
            - Create superclass of init
            - Create array of keys
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache using LRU
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

            self.keys.append(self.keys.pop(self.keys.index(key))) \
                if key in self.keys else self.keys.append(key)

            if len(self.keys) > BaseCaching.MAX_ITEMS:
                l = self.keys.pop(0)
                del self.cache_data[l]
                print("DISCARD: {:s}".format(l))

    def get(self, key):
        """ Get an item by key using LRU
        """
        if not key or key not in self.cache_data:
            return None
        self.keys.append(self.keys.pop(self.keys.index(key)))
        return self.cache_data[key]
