"""
Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20 x 20 grid?
"""

from euler.math import binomial_coefficient


def solve():
    # There are 20 steps possible for both right and down directions, so 40 total possible steps.
    # So find the binomial coefficient picking 20 different possible steps out of 40 possible steps.
    return binomial_coefficient(40, 20)


if __name__ == "__main__":
    print(solve())
