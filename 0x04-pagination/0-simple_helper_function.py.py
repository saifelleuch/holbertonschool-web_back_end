#!/usr/bin/env python3
"""0-simple_helper_function.py"""


def index_range(page, page_size):
    """
    a function named index_range that
    takes two integer arguments page
    and page_size.
    """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
