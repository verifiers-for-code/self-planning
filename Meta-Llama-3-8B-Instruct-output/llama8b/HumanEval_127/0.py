def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    """Calculate the intersection of two intervals and check if its length is a prime number"""
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    if start > end:
        return "NO"
    intersection_length = end - start + 1
    if is_prime(intersection_length):
        return "YES"
    return "NO"