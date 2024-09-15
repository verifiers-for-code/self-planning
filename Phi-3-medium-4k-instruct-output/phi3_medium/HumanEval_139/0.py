def factorial(n):
    """Calculate the factorial of a given number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def special_factorial(n):
    """Calculate the Brazilian factorial of a given number."""
    result = 1
    for i in range(1, n+1):
        result *= factorial(i)
    return result