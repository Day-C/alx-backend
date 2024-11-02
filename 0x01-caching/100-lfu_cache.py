#!/usr/bin/env python3
"""fifo caching systm."""
from ase_caching import BaseCaching


class LFUCache (BaseCaching):
    """fifi cache."""
    
    def __init__(self):
        """initialize super values."""
        
        super().__init__()
        
    def put(self, key, item):
        """add a new cache."""
        
        if len(self.cache_data) <= self.MAX_ITEMS:
            if key is not None or item is not None:
                self.cache_data[key] = item
        else:
            first = self.cache_data.items()
            for key in self.cache_data.keys():
                print(f"DISCARD: {key}")
                del self.cache_data[key]
                break
        
    def get(self, key):
        """display cache."""

        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
