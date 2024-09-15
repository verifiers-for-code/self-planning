from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    # Create a new list
    new_list = []
    
    # Loop through the input list
    for i in range(len(numbers)):
        # Append the current element to the new list
        new_list.append(numbers[i])
        
        # Append the delimeter to the new list, except for the last element
        if i != len(numbers) - 1:
            new_list.append(delimeter)
    
    # Return the new list
    return new_list