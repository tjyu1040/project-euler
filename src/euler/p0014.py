"""
Which starting number, under one million, produces the longest chain?
"""

from collections.abc import Iterator


def solve():
    longest_chain = 0
    starting_number = 1
    for i in range(1, 1000001):
        chain_length = len(list(collatz(i)))
        if chain_length > longest_chain:
            longest_chain = chain_length
            starting_number = i
    return starting_number


def collatz(n: int) -> Iterator[int]:
    if n < 1:
        raise ValueError(f"n must be a positive integer: {n}")
    yield n
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        yield n


if __name__ == "__main__":
    print(solve())
