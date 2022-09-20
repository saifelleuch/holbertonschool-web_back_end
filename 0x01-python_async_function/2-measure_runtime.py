#!/usr/bin/env python3
"""run_time"""

import asyncio
import random
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    [run time]
    Args:
        n (int): number
        max_delay (int, optional): max
    Returns:
        float: res
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n
