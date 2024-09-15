def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    i = 2
    while n > 1:
        if n % i == 0:
            if is_prime(i):
                return i
            while n % i == 0:
                n //= i
        i += 1
    return 1