#!/usr/bin/python3
""" Create a class BasicCache that inherits
from BaseCaching and is a caching system """

BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """ caching system """
    def __init__(self) -> None:
        super().__init__()


    def put(self, key, item):
        """ Must assign to the dictionary self.cache_data
            the item value for the key
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Must return the value in self.cache_data linked to key """
        if key:
            try:
                return.self.cache_data(key)
            except keyError:
                return None
