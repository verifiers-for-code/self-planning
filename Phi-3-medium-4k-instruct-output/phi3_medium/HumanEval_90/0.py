def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    # Remove duplicates from the list
    lst = list(set(lst))
    
    # Sort the list
    lst.sort()
    
    # If the length of the list is less than 2, return None
    if len(lst) < 2:
        return None
    
    # Return the second element of the list
    return lst[1]