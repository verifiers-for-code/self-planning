from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create an empty list to store the result
    result = []
    
    # Create a dictionary to store the frequency of each number
    frequency = {}
    
    # Loop through the input list
    for num in numbers:
        # If the frequency of the number is 1, append it to the result list
        if num not in frequency:
            frequency[num] = 1
            result.append(num)
        # If the frequency of the number is more than 1, do nothing
        else:
            frequency[num] += 1
    
    # Return the result list
    return result