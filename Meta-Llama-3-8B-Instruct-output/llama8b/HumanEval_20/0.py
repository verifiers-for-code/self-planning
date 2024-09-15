from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Step 1: Sort the list of numbers
    numbers.sort()
    
    # Step 2: Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')
    closest_pair = (None, None)
    
    # Step 3: Loop through the sorted list, comparing each pair of adjacent numbers
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i-1]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i-1], numbers[i])
    
    return closest_pair