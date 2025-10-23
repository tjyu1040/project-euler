"""
There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
"""


def solve():
    for c in range(1, 1000):
        for a in range(1, c):
            b = 1000 - c - a
            if a**2 + b**2 == c**2:
                return a * b * c
    raise AssertionError("No product found for a Pythagorean triplet for which a + b + c = 1000")


if __name__ == "__main__":
    print(solve())
