#!/usr/bin/env python3
"""Creates a asyncio task"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: float) -> asyncio.Task:
    """Creates an asyncio Task"""
    return asyncio.create_task(wait_random(max_delay))
