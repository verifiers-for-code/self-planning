def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_digits(n):
    """Sum the digits of a number."""
    return sum(int(digit) for digit in str(n))

def largest_prime_sum(lst):
    """Find the largest prime value and return the sum of its digits."""
    primes = [num for num in lst if is_prime(num)]
    if not primes:
        return 0
    largest_prime = max(primes)
    return sum_of_digits(largest_prime)