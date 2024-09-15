from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize an empty list to store the rolling maximums.
    rolling_maximums = []
    # Initialize a variable to keep track of the current maximum.
    current_max = float('-inf')
    # Loop through the input list.
    for num in numbers:
        # For each element, compare it with the current maximum.
        if num > current_max:
            # If the element is greater than the current maximum, update the current maximum and append it to the rolling maximums list.
            current_max = num
            rolling_maximums.append(current_max)
        else:
            # If the element is less than or equal to the current maximum, just append the current maximum to the rolling maximums list.
            rolling_maximums.append(current_max)
    # Return the rolling maximums list.
    return rolling_maximums