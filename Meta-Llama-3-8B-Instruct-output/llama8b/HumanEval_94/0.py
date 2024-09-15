def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_digits(n):
    """Calculate the sum of the digits of a number."""
    return sum(int(digit) for digit in str(n))

def largest_prime_sum(lst):
    """Find the largest prime number in the list and return the sum of its digits."""
    max_prime = max((num for num in lst if is_prime(num)), default=0)
    return sum_of_digits(max_prime)