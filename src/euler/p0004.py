"""
Find the largest palindrome made from the product of two 3-digit numbers.
"""

import numpy as np


def is_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]


def solve():
    three_digits_numbers = np.arange(100, 1000)
    product_numbers = np.outer(three_digits_numbers, three_digits_numbers).ravel()
    product_numbers.sort()
    for product_number in reversed(product_numbers):
        if is_palindrome(product_number):
            return product_number
    raise AssertionError("No palindrome made from the product of two 3-digit numbers found.")


if __name__ == "__main__":
    print(solve())
