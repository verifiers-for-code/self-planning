from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    result = []
    max_so_far = float('-inf')
    for num in numbers:
        if num > max_so_far:
            max_so_far = num
        result.append(max_so_far)
    return result