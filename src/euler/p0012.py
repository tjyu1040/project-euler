"""
What is the value of the first triangle number to have over five hundred divisors?
"""

from euler.math import find_prime_factors


def solve():
    i = 1
    while True:
        triangle_number = calculate_triangle_number(i)
        num_divisors = get_number_of_divisors(triangle_number)
        if num_divisors >= 500:
            return triangle_number
        i += 1


def calculate_triangle_number(n: int) -> int:
    return n * (n + 1) // 2


def get_number_of_divisors(n: int) -> int:
    prime_factors = find_prime_factors(n)
    num_divisors = 1
    for prime_factor in set(prime_factors):
        exponent = prime_factors.count(prime_factor)
        num_divisors *= exponent + 1
    return num_divisors


if __name__ == "__main__":
    print(solve())
