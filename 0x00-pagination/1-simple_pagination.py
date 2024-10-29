#!/usr/bin/env python3
"""pagination object."""
import csv
import math
from typing import List


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get paginated data based on input."""

        assert type(page) is int and page > 0, "page must be an int & > 0"
        assert type(page_size) is int and page_size > 0, "must be int"
        idx_range = index_range(page, page_size)
        if idx_range[0] > 19419 or idx_range[1] > 19419:
            return []
        result = []
        # print(f"{idx_range[0]} {idx_range[1]}")
        # get api request
        data = self.dataset()
        for i in range(idx_range[0], idx_range[1]):
            result.append(data[i])
        return result
