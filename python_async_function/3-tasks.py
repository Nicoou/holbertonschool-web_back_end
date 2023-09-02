#!/usr/bin/env python3
"""task 3"""
import asyncio
from typing import List
import time
from asyncio import Task


def task_wait_random(max_delay: int) -> Task:
    """task def"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    return asyncio.create_task(wait_random(max_delay))
