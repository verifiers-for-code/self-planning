from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Subtract the minimum from each number in the list
    numbers = [num - min_val for num in numbers]

    # Divide each number by the range (max - min)
    range_val = max_val - min_val
    numbers = [num / range_val for num in numbers]

    # Return the transformed list
    return numbers