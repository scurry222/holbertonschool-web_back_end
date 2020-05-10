#!/usr/bin/python3
""" LIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Class LIFOCache

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
        """ Add an item in the cache using LIFO
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

            self.keys.append(self.keys.pop(self.keys.index(key))) \
                if key in self.keys else self.keys.append(key)

            if len(self.keys) > BaseCaching.MAX_ITEMS:
                f = self.keys.pop(len(self.keys) - 2)
                del self.cache_data[f]
                print("DISCARD: {:s}".format(f))

    def get(self, key):
        """ Get an item by key using LIFO
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
