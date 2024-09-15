import math

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    # 1. If n is less than 2, return False.
    if n < 2:
        return False

    # 2. Loop from 2 to the square root of n.
    for i in range(2, int(math.sqrt(n)) + 1):
        # 3. If n is divisible by any number in the loop, return False.
        if n % i == 0:
            return False

    # 4. If no divisor is found, return True.
    return True