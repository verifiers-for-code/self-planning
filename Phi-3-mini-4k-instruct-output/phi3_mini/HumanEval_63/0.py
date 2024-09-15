def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fib_sequence(n):
    """Generate a Fibonacci sequence."""
    fib = [0, 0, 1]
    for i in range(3, n + 1):
        fib.append(fib[i - 1] + fib[i - 2] + fib[i - 3])
    return fib

def fibfib(n):
    """Compute the n-th element of the fibfib number sequence."""
    fib = fib_sequence(n)
    count = 0
    for num in fib:
        if is_prime(num):
            count += 1
    if count == 0:
        return fib[n]
    else:
        return -1