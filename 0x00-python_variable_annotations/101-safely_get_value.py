#!/usr/bin/env python3
"""101-safely_get_value.py"""

from typing import Union, Mapping, Any, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    get val
    Args:
        dct(Mapping): mapping
        key(Any): any type
        default(Union[T, None], optional): Default to None.
    Returns:
        Union[Any, T]: union of any and typevar T
    """
    if key in dct:
        return dct[key]
    else:
        return default
