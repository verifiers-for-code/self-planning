def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Check if the list is empty or has only one element. If so, return True.
    if len(l) <= 1:
        return True

    # Determine if the list is increasing or decreasing.
    is_increasing = l[0] < l[1]
    is_decreasing = l[0] > l[1]

    # Loop through the list and check if the list is monotonically increasing or decreasing.
    for i in range(1, len(l)):
        if is_increasing and l[i] < l[i-1]:
            return False
        if is_decreasing and l[i] > l[i-1]:
            return False

    # Return True if the list is monotonically increasing or decreasing, otherwise return False.
    return True