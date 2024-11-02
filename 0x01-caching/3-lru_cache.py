#!/usr/bin/python3
"""implement a lruu chaching system."""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Least Recently Used(LRC) cahe system."""
    
    def __init__(self):
        """initialize parent attributes."""
        
        super().__init__()
        
    def put(self, key, item):
        """add a new cach element."""
        
        if key is not None and item is not None:
            if len(self.cache_data) > self.MAX_ITEMS:
