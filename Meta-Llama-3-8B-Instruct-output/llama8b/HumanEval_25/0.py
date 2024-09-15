from typing import List

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors"""
    factors = []
    i = 2
    while n > 1:
        if n % i == 0 and is_prime(i):
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            factors.append(i * [i])
        i += 1
    return factors