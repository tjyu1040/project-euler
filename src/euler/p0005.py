"""
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from functools import reduce

import numpy as np


def gcd(a: int, b: int) -> int:
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    return int(np.abs(a * b) / gcd(a, b))


def solve():
    smallest_number_divisible = reduce(lcm, np.arange(1, 21, dtype=int))
    return smallest_number_divisible


if __name__ == "__main__":
    print(solve())
