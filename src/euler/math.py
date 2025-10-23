from math import factorial, sqrt


def is_prime_number(n: int) -> bool:
    """
    Check if `n` is a prime number.
    :param n: The integer to check.
    :return: True if n is a prime number, False otherwise.
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        while i**2 <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True


def find_prime_factors(n: int) -> list[int]:
    """
    Find all prime factors of `n`.
    :param n: The positive integer to find prime factors for.
    :return: The list of prime factors of `n`.
    """
    if n < 1:
        raise ValueError("n must be a positive integer.")
    if n == 1:
        return []

    prime_factors = []
    # Add even numbers that divides n.
    while n % 2 == 0:
        prime_factors.append(2)
        n /= 2

    # Add odd numbers that divides n.
    # For the limit, every composite number has at least one prime factor less than or
    # equal to square root of itself.
    limit = int(sqrt(n) + 1)
    for i in range(3, limit, 2):
        while n % i == 0:
            prime_factors.append(i)
            n /= i

    # n is now either 1 or a prime number.
    if n > 2:
        prime_factors.append(n)

    return sorted(prime_factors)


def binomial_coefficient(n: int, k: int) -> int:
    """
    The binomial coefficient (`n`, `k`) is the number of ways of picking `k` unordered outcomes from
    `n` possibilities, also known as a combination or combinatorial number.
    :param n: The non-negative number of possible outcomes.
    :param k: The non-negative number of unordered outcomes to pick.
    :return: The binomial coefficient.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    if k < 0:
        raise ValueError("k must be a non-negative integer.")
    return factorial(n) // (factorial(k) * factorial(n - k))
