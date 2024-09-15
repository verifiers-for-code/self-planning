from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1"""
    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)
    
    # Calculate the range of the list
    range_val = max_val - min_val
    
    # Create a new list where each element is the difference between the element and the minimum value divided by the range
    rescaled_list = [(num - min_val) / range_val for num in numbers]
    
    return rescaled_list