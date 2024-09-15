def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    convertString = "0123456789ABCDEF"
    if x < base:
        return convertString[x]
    else:
        return change_base(x // base, base) + convertString[x % base]