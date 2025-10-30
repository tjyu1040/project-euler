"""
What is the sum of the digits of the number 2 ** 1000?
"""


def solve():
    return digit_sum(2**1000)


def digit_sum(n: int) -> int:
    return sum(int(digit) for digit in str(n))


if __name__ == "__main__":
    print(solve())
