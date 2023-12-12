#!/usr/bin/env python3
"""Introduces the Basic syntax of asyncio to perform concurrency"""

wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
import random
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Runs the wait_random coroutine ntimes"""
    wait_times = []
    for x in range(n):
        delay = await wait_random(max_delay)
        wait_times.append(delay)
    return wait_times