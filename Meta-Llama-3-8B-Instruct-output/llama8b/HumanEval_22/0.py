from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers """
    filtered_list = []  # 1. Create an empty list to store the filtered integers.
    for value in values:  # 2. Loop through the input list.
        if isinstance(value, int):  # 3. Check if the current element is an integer, if yes, append it to the filtered list.
            filtered_list.append(value)
    return filtered_list  # 4. Return the filtered list.