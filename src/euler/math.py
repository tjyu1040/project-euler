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
