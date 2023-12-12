#!/usr/bin/env python3
""" Contains a asynchronous generator function. """

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    """ A Async Generator for 10 random numbers. """
    for run in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
