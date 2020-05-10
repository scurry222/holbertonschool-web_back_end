#!/usr/bin/python3
""" FIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Class FIFOCache

        Attributes:
            - Inherits from BaseCaching
            - Discard last item in queue first
    """

    def __init__(self):
        """ Initialize
            - Create superclass of init
            - Create array of keys
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache using FIFO
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                f = self.keys.pop(0)
                del self.cache_data[f]
                print("DISCARD: {:s}".format(f))

    def get(self, key):
        """ Get an item by key using FIFO
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
