def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # 1. Create a set from the list to remove duplicates.
    unique_set = set(l)
    
    # 2. Convert the set back to a list.
    unique_list = list(unique_set)
    
    # 3. Sort the list.
    unique_list.sort()
    
    # 4. Return the sorted list.
    return unique_list