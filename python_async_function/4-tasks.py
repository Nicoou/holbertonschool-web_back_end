#!/usr/bin/env python3
"""task 0"""
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """task def"""
    wait_random = __import__('3-tasks').wait_random
    task = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*task)

    return sorted(delays)