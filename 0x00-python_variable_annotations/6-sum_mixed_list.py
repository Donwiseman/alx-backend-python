#!/usr/bin/env python3
"""Contains a the sum_mixed_list function that returns the sum of elements in
   the passed list argument. """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """Returns the sum of a given list"""
    return sum(mxd_lst)
