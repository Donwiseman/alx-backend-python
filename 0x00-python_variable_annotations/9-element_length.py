#!/usr/bin/env python3
"""Contains a function that takes an iterable containing sequences
   and returns a list"""

from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes an iterable of sequences and return a list containing a tuple"""
    return [(i, len(i)) for i in lst]
