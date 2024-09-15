def is_simple_power(x, n):
    """
    This function returns true if a number x is a simple power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    # Check if x is less than or equal to 1. If it is, return False.
    if x <= 1:
        return False

    # Loop from 2 to x.
    for i in range(2, x + 1):
        # Check if x is divisible by n.
        if x % n == 0:
            # If it is, divide x by n and continue the loop.
            x = x // n
        else:
            # If it is not, return False.
            return False

    # If the loop completes, return True.
    return True