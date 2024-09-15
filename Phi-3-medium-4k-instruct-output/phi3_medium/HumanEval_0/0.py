from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # Step 1: Sort the list of numbers
    numbers.sort()

    # Step 2: Loop through the list, compare the difference between adjacent numbers
    for i in range(len(numbers) - 1):
        # Step 3: If the difference is less than the threshold, return True
        if abs(numbers[i] - numbers[i + 1]) < threshold:
            return True

    # Step 4: If no such pair is found, return False
    return False