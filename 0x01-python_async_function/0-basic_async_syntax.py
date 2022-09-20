#!/usr/bin/env python3
""" random time to wait """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    [this function will make a random delay]

    Args:
        max_delay (int, optional): max

    Returns:
        Float: random time to wait
    """

    rand_wt = random.uniform(0, max_delay)
    await asyncio.sleep(rand_wt)
    return rand_wt
