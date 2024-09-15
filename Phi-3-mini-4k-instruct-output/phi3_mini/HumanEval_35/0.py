def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # Create a variable to store the maximum value
    max_value = l[0]

    # Loop the list
    for element in l:
        # If the current element is greater than the maximum value, set the maximum value to the current element
        if element > max_value:
            max_value = element

    # Return the maximum value
    return max_value