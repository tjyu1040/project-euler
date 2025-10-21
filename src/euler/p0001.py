"""
Find the sum of all the multiples of 3 or 5 below 1000.
"""

import numpy as np


def solve():
    numbers = np.arange(1000)
    multiples_of_3_or_5 = (numbers % 3 == 0) | (numbers % 5 == 0)
    sum_of_multiples = numbers[multiples_of_3_or_5].sum()
    return sum_of_multiples


if __name__ == "__main__":
    print(solve())
