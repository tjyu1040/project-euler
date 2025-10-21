"""
What is the largest prime factor of the number 600851475143?
"""

import numpy as np
import numpy.typing as npt


def find_prime_factors(n: int) -> npt.NDArray[int]:
    prime_factors = []
    # Add even numbers that divides n.
    while n % 2 == 0:
        prime_factors.append(2)
        n /= 2

    # Add odd numbers that divides n.
    # For the limit, every composite number has at least one prime factor less than or
    # equal to square root of itself.
    limit = int(np.sqrt(n) + 1)
    for i in range(3, limit, 2):
        while n % i == 0:
            prime_factors.append(i)
            n /= i

    # n is now either 1 or a prime number.
    if n > 2:
        prime_factors.append(n)

    return np.array(sorted(prime_factors))


def solve():
    prime_factors = find_prime_factors(600851475143)
    return max(prime_factors)


if __name__ == "__main__":
    print(solve())
