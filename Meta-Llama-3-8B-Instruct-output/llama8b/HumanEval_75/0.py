def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Check if a number is the multiplication of 3 prime numbers."""
    for i in range(2, int(a**0.5) + 1):
        if is_prime(i):
            for j in range(i, int(a/i) + 1):
                if is_prime(j) and i * j == a:
                    for k in range(j, int(a/(i*j)) + 1):
                        if is_prime(k) and i * j * k == a:
                            return True
    return False