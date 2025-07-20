#!/usr/bin/python3
""" Create a class LIFOCache that inherits
from BaseCaching and is a caching system """

BaseCaching = __import__('base_caching').BaseCaching

class LIFOCache(BaseCaching):
    """ LIFO cache """

    def __init__(self) -> None:
        """ SUPER INIT """
        super().__init__()

    def put(self, key, item) -> None:
        """ Must assign to cache_data the item value for key """
        if key and item:
            if key in list(self.cache_data.keys()):
                del self.cache_data[key]
            if (len(self.cache_data.keys()) == self.MAX_ITEMS):
                k = list(self.cache_data.keys()).pop
                del self.cache_data[k]
                print("DISCARD: {}".format(k))
            self.cache_data[key] = item


    def get(self, key):
        """ return value in self cache data """
        if key:
            try:
                return self.cache_data.get(key)
            except KeyError:
                return None
        return None
