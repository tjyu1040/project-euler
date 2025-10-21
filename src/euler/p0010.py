"""
Find the sum of all the primes below two million.
"""

import numpy as np

from euler.math import is_prime_number


def solve():
    primes = []
    for i in range(2, 2000000):
        if is_prime_number(i):
            primes.append(i)
    primes = np.array(primes, dtype=np.int64)
    return primes.sum()


if __name__ == "__main__":
    print(solve())
