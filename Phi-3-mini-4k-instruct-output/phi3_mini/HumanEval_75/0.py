import math

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Return True if the given number is the multiplication of 3 prime numbers, False otherwise."""
    if a < 100:
        count = 0
        for i in range(2, int(math.sqrt(a)) + 1):
            if a % i == 0 and is_prime(i) and is_prime(a // i):
                count += 1
                if count == 3:
                    return True
        return False
    else:
        return False