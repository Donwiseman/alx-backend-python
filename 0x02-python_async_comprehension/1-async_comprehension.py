#!/usr/bin/env python3
"""A function that uses an async generator to create ten numbers"""

from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Uses an async generator to return a list of ten numbers"""
    return [num async for num in async_generator()]
