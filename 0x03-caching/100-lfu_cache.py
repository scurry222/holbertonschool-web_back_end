#!/usr/bin/python3
""" MRUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ Class MRUCache

        Attributes:
            - Inherits from BaseCaching
            - Discard most recently used items first
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize
            - Create superclass of init
            - Create array of keys
        """
        super().__init__()
        self.keys = []
        self.freq = {}

    def put(self, key, item):
        """ Add an item in the cache using MRU
        """
        if key or item:
            if len(self.keys) >= BaseCaching.MAX_ITEMS and\
                 key not in self.keys:
                m = self.keys.pop(self.keys.index(self.find_LFU()))
                del self.freq[m]
                del self.cache_data[m]
                print("DISCARD: {:s}".format(m))

            self.cache_data[key] = item

            if key in self.keys:
                self.keys.append(self.keys.pop(self.keys.index(key)))
                self.freq[key] += 1
            else:
                self.keys.append(key)
                self.freq[key] = 0

    def get(self, key):
        """ Get an item by key Using MRU
        """
        if not key or key not in self.cache_data:
            return None
        self.keys.append(self.keys.pop(self.keys.index(key)))
        self.freq[key] += 1
        return self.cache_data[key]

    def find_LFU(self):
        """ Return first occurence of lowest frequency value
        """
        m = min(self.freq.values())
        for key in self.freq:
            if self.freq[key] == m:
                return key
        return None
