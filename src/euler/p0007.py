"""
What is the 10,001st prime number?
"""

from euler.math import is_prime_number


def solve():
    prime_count = 0
    number = 0
    while prime_count != 10001:
        number += 1
        if is_prime_number(number):
            prime_count += 1
    return number


if __name__ == "__main__":
    print(solve())
