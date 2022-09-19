#!/usr/bin/env python3
"""100-safe_first_element.py"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    uknown
    Args:
        lst(Sequence[Any]): any typed list
    Returns:
        Union[Any, None]: first of  list or none
    """
    if lst:
        return lst[0]
    else:
        return None
