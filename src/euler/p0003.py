"""
What is the largest prime factor of the number 600851475143?
"""

from euler.math import find_prime_factors


def solve():
    prime_factors = find_prime_factors(600851475143)
    return max(prime_factors)


if __name__ == "__main__":
    print(solve())
