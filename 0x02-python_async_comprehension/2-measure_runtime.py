#!/usr/bin/env python3
"""Measures the runtime of four async_comprehension call"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the time to run for async_comprehension call"""
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    runtime = time.perf_counter() - start
    return runtime
