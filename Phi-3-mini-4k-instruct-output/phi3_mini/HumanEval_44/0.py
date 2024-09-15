def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    # Create a list to store the digits
    digits = []

    # While x is greater than 0, append the remainder of x divided by base to the list
    while x > 0:
        digits.append(x % base)
        x //= base

    # Reverse the list
    digits.reverse()

    # Join the list into a string and return it
    return ''.join(str(digit) for digit in digits)