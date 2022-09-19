#!/usr/bin/env python3
"""7-to_kv.py"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Make a tuple
    Args:
        k(str): first item of the tuple
        v(Union[int, float]): second item of the tuple
    Returns:
        tuple: res
    """
    return (k, v**2)
