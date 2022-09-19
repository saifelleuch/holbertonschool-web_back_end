#!/usr/bin/env python3
"""102-type_checking.py"""

from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    zoom_array
    Args:
        lst(Tuple): tuple
        factor (int, optional): factor Defaults to 2.
    Returns:
        List: [final list]
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), int(3.0))
