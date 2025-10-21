import pytest

from euler.math import is_prime_number


def test_zero_is_not_prime_number():
    assert not is_prime_number(0)


@pytest.mark.parametrize("prime_number", [2, 3, 5, 7, 11, 13, 17, 19])
def test_is_prime_number(prime_number: int):
    assert is_prime_number(prime_number)


@pytest.mark.parametrize("non_prime_number", [1, 4, 6, 8, 9, 10, 12, 15, 16, 18, 20] + list(range(-1, -21, -1)))
def test_is_not_prime_number(non_prime_number: int):
    assert not is_prime_number(non_prime_number)
