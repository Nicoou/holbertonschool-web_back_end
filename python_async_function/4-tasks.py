#!/usr/bin/env python3
"""task 0"""
import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """task def"""
    task_wait_random = __import__('3-tasks').task_wait_random
    task = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*task)

    return sorted(delays)
