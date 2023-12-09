#!/usr/bin/env python3
"""Contains a the to_kv function that returns a tuple formed from
   passesd parameters."""

from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple made from parameters"""
    return (k, (v * v))
