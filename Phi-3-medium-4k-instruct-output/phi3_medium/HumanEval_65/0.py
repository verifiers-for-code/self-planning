def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert the integer to a string
    x_str = str(x)
    
    # If shift is greater than the length of the string, reverse the string
    if shift > len(x_str):
        return x_str[::-1]
    
    # Otherwise, shift the string to the right by the shift amount
    else:
        shifted_str = x_str[-shift:] + x_str[:-shift]
        return shifted_str