def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # 1. Initialize max_element to the first element of the list.
    max_element = l[0]

    # 2. Loop through the list, if the current element is greater than max_element, update max_element.
    for element in l:
        if element > max_element:
            max_element = element

    # 3. Return max_element.
    return max_element