#!/usr/bin/env python3
"""
Task 9 - element lenght function
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element_length func"""
    return [(n, len(n)) for n in lst]
