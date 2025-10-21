"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

import numpy as np


def solve():
    phi = (1 + np.sqrt(5)) / 2
    index = np.log(4000000 * np.sqrt(5) + 0.5) / np.log(phi)
    numbers = np.arange(1, index)
    fibonacci_sequence = (phi**numbers - (-1 / phi) ** numbers) / np.sqrt(5)
    fibonacci_sequence = fibonacci_sequence.astype(int)
    sum_even_fib_terms = fibonacci_sequence[fibonacci_sequence % 2 == 0].sum()
    return sum_even_fib_terms


if __name__ == "__main__":
    print(solve())
