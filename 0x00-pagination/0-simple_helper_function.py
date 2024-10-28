#!/usr/bin/env python3
"""pagination page and size."""


def index_range(page: int, page_size: int) -> tuple:
    """set the starting index and end index curresponding
    to the range of index:"""

    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return (start_idx, end_idx)
