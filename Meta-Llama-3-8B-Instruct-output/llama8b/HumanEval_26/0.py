from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    result = []
    frequency = {}
    
    for num in numbers:
        if num not in frequency or frequency[num] == 1:
            result.append(num)
            frequency[num] = frequency.get(num, 0) + 1
    
    return result