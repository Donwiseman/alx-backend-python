#!/usr/bin/env python3
"""Introduces the Basic syntax of asyncio to perform concurrency"""

wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Runs the wait_random coroutine ntimes"""
    wait_times = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return wait_times