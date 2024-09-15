import math

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Check if a number is the multiplication of 3 prime numbers."""
    prime_factors = []
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0 and is_prime(i):
            prime_factors.append(i)
            a = a // i
    if a > 1 and is_prime(a):
        prime_factors.append(a)
    return len(prime_factors) == 3