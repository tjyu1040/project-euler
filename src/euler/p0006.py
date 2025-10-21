"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

import numpy as np


def solve():
    sum_of_squares = (np.arange(1, 101) ** 2).sum()
    squared_sum = np.arange(1, 101).sum() ** 2
    sum_squares_diff = squared_sum - sum_of_squares
    return sum_squares_diff


if __name__ == "__main__":
    print(solve())
