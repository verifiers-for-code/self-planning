def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_digits(n):
    """Calculate the sum of digits of a number."""
    return sum(int(digit) for digit in str(n))

def skjkasdkd(lst):
    """Find the largest prime value in a list and return the sum of its digits."""
    largest_prime = None
    for num in lst:
        if is_prime(num):
            if largest_prime is None or num > largest_prime:
                largest_prime = num
    if largest_prime is None:
        return 0
    return sum_of_digits(largest_prime)