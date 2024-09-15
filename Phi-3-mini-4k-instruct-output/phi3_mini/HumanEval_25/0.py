from typing import List
import math

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    # Divide the input number by 2 until it is odd
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Loop from 3 to the square root of the input number, incrementing by 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    # If the input number is greater than 2, append it to the list of prime factors
    if n > 2:
        factors.append(n)
    return factors