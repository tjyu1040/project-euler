"""
Find the sum of all the primes below two million.
"""

from euler.math import is_prime_number


def solve():
    primes = []
    for i in range(2, 2000000):
        if is_prime_number(i):
            primes.append(i)
    return sum(primes)


if __name__ == "__main__":
    print(solve())
