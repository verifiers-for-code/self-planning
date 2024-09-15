from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # 1. Initialize an empty list to store the rolling maximum.
    rolling_max_list = []

    # 2. Initialize a variable to store the current maximum.
    current_max = float('-inf')

    # 3. Iterate over the list of numbers.
    for num in numbers:
        # 4. For each number, if it is greater than the current maximum, update the current maximum and append it to the rolling maximum list.
        if num > current_max:
            current_max = num
        # 5. If it is not greater than the current maximum, append the current maximum to the rolling maximum list.
        rolling_max_list.append(current_max)

    # 6. Return the rolling maximum list.
    return rolling_max_list