#!/usr/bin/env python3
"""
Task 5 - sum list function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """func sum_list"""
    x = 0.0
    for n in input_list:
        x = n + x
    return x
