#!/usr/bin/python3
""" Create a class FIFOCache that inherits
from BaseCaching and is a caching system """

class FIFOcache(BaseCaching):
    """ FiFo Cache """
    def __init__(self) -> None:
        """ SUPER INIT """
        super()__init__()


    def put(self, key, item) -> None:
        """ Assign to cache_data the item value """
        if key and item:
            if (len(self.cache_data.keys()) == self.MAX_ITEMS):
                k = list(self.cache_data.keys())[0]
                del self.cache_data[k]
                print("DISCARD: {}".format(k))
            self.cache_data.update({key: item})


    def get(self, key):
        """ Must return the value in self cache data to key """
        if key:
            try:
                return self.cache_data(key)
            except KeyError:
                return None
        return None
