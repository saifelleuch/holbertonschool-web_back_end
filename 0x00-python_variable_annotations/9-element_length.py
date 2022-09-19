#!/usr/bin/env python3
"""9-element_length.py"""

from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    iterable
    Args:
        lst(Iterable[Sequence]): a list
    Returns:
        List[Tuple[Sequence, int]]: list
    """
    return [(i, len(i)) for i in lst]
