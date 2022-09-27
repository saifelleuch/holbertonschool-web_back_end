#!/usr/bin/env python3
"""0. Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index_range that takes two
    integer arguments page and page_size
    """
    return (page * page_size - page_size, page * page_size)
