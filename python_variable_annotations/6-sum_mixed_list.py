#!/usr/bin/env python3
"""
Task 6 - sum mixed list function
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """func sum_mixed_list"""
    x = 0.0
    for n in mxd_lst:
        x = n + x
    return x
