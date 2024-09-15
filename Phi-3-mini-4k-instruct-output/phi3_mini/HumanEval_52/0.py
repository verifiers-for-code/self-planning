def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
    Loop the list.
    If any number is greater than or equal to the threshold, return False.
    Return True."""
    for num in l:
        if num >= t:
            return False
    return True