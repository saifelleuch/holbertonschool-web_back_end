#!/usr/bin/env python3
"""2. Hypermedia pagination
"""
from typing import Tuple, List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index_range that takes two
    integer arguments page and page_size.
    """
    return (page * page_size - page_size, page * page_size)


class Server:
    """server class to paginate a
    database of popular baby names.
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
        """get_page that takes two integer
        arguments page with default
        value 1 and page_size with default value 10.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        first, last = index_range(page, page_size)
        dataset = self.dataset()
        if first > len(dataset):
            return []
        return self.dataset()[first:last]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """method that takes the same arguments
        (and defaults) as get_page and returns
        a dictionary containing the following
        key-value pairs:
        """
        total = math.floor(len(self.dataset()) / page_size)
        return {
            "page_size": len(self.get_page(page, page_size)),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page + 1 < total else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total
        }
