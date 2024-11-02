#!/usr/bin/env python3
"""implement a lofo chaching system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """last in first out caching system."""

    def __init__(self):
        """initiaize parent attributes."""

        super().__init__()

    def put(self, key, item):
        """add new cache in to the casching system."""

        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
                self.cache_data[key] = item
            elif len(self.cache_data) == self.MAX_ITEMS:
                rm_key = self.cache_data.popitem()
                print(f"DISCARD: {rm_key[0]}")
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """show the vale of a chached key"""

        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
