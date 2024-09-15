def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    

 1. Check if x is equal to n raised to the power of an integer.
2. Return True if x is a simple power of n, otherwise return False."""
    if x == 1:
        return True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            power = 0
            while x % i == 0:
                x //= i
                power += 1
            if i == n and power > 1:
                return True
    return x == n and x > 1