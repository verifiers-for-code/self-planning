def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    # 1. Create a new list.
    positive_numbers = []
    
    # 2. Loop through the input list.
    for num in l:
        # 3. If the number is positive, append it to the new list.
        if num > 0:
            positive_numbers.append(num)
    
    # 4. Return the new list.
    return positive_numbers