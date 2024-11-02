#!/usr/bin/env python3
"""fifo caching systm."""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """fifi cache."""

    def __init__(self):
        """initialize super values."""

        super().__init__()

    def put(self, key, item):
        """add a new cache."""

        if key is not None or item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                rm_key = ''
                for key in self.cache_data.keys():
                    rm_key = key
                    break
                del self.cache_data[rm_key]
                print(f"DISCARD: {rm_key}")

    def get(self, key):
        """display cache."""

        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
