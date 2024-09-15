from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Step 1: Sort the list of numbers
    numbers.sort()

    # Step 2: Initialize the minimum difference to a large number
    min_diff = float('inf')

    # Step 3: Loop through the list and calculate the difference between each pair of adjacent numbers
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]

        # Step 4: If the difference is less than the minimum difference, update the minimum difference and store the pair of numbers
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    # Step 5: Return the pair of numbers
    return closest_pair