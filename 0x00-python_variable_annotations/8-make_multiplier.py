#!/usr/bin/env python3
"""Contains a function that returns a callable."""

from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a Callable that multiplies a given parameter"""
    def fun(number: float) -> float:
        """A function that multiplies passed parameter by a factor"""
        return number * multiplier
    return fun
