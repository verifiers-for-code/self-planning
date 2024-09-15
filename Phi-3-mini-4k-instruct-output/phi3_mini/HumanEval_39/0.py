def is_prime(num):
    """
    Check if a number is prime.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def fibonacci(n):
    """
    Generate the nth Fibonacci number.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def prime_fib(n):
    """
    Return the nth Fibonacci number that is also prime.
    """
    count = 0
    num = 0
    while count < n:
        num = fibonacci(num)
        if is_prime(num):
            count += 1
    return num