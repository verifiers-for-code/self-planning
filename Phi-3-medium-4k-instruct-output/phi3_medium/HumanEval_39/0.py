from typing import List

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n: int) -> List[int]:
    """Generate a Fibonacci sequence."""
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def prime_fib(n: int) -> int:
    """Return the n-th number that is a Fibonacci number and it's also prime."""
    counter = n
    fib_seq = fibonacci(n * 10)  # Generate a large Fibonacci sequence
    for num in fib_seq:
        if is_prime(num):
            counter -= 1
            if counter == 0:
                return num