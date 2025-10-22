import pytest

from euler.math import find_prime_factors, is_prime_number


def integer_id(integer: int) -> str:
    """Parametrized ID generator for an integer value."""
    return f"n={integer}"


@pytest.mark.parametrize("prime_number", [2, 3, 5, 7, 11, 13, 17, 19], ids=integer_id)
def test_is_prime_number(prime_number: int):
    assert is_prime_number(prime_number)


@pytest.mark.parametrize(
    "non_prime_number", [0, 1, 4, 6, 8, 9, 10, 12, 15, 16, 18, 20] + list(range(-1, -21, -1)), ids=integer_id
)
def test_is_not_prime_number(non_prime_number: int):
    assert not is_prime_number(non_prime_number)


@pytest.mark.parametrize("invalid_number", list(range(0, -21, -1)), ids=integer_id)
def test_find_prime_factors_invalid_number(invalid_number: int):
    with pytest.raises(ValueError):
        find_prime_factors(invalid_number)


def test_find_prime_factors():
    assert find_prime_factors(1) == []
    assert find_prime_factors(2) == [2]
    assert find_prime_factors(3) == [3]
    assert find_prime_factors(4) == [2, 2]
    assert find_prime_factors(5) == [5]
    assert find_prime_factors(6) == [2, 3]
    assert find_prime_factors(7) == [7]
    assert find_prime_factors(8) == [2, 2, 2]
    assert find_prime_factors(9) == [3, 3]
    assert find_prime_factors(10) == [2, 5]
