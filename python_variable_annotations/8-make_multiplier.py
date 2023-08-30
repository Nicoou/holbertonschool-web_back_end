#!/usr/bin/env python3
"""
Task 8 - make multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a function that multiplies"""
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return multiplier_func
