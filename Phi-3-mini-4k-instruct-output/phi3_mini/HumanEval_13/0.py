def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    

 1. If b is 0, return a.
2. Otherwise, return the greatest common divisor of b and the remainder of a divided by b.
3. Repeat until b is 0."""
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)