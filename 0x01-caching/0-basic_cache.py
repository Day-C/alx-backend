#!/usr/bin/env python3
"""caching system."""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """simple caching asystem."""

    def __init__(self):
        """Initialize super var."""

        super().__init__()

    def put(self, key, item):
        """Create a cache."""

        # add a new key[item] into the dictionary cache_data
        self.cache_data[key] = item

    def get(self, key):
        """return the value of key."""

        # retrive the value of a cached key
        if key in self.cache_data and self.cache_data[key] is not None:
            return self.cache_data[key]
        return None
