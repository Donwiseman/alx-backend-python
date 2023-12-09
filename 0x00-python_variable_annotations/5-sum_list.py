#!/usr/bin/env python3
"""Contains a the sum_list function that returns the sum of a float elemen in
   the passed list argument. """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of a given list"""
    return sum(input_list)
