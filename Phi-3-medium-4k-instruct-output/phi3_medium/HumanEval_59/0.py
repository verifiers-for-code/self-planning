def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n."""
    largest_prime = 1
    # Divide n by 2 until it's odd
    while n % 2 == 0:
        largest_prime = 2
        n //= 2
    # Check for odd factors
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            largest_prime = i
            n //= i
    # If n is a prime number greater than 2
    if n > 2:
        largest_prime = n
    return largest_prime