from typing import List

def sort_numbers(numbers: str) -> str:
    # Create a dictionary to map the string numbers to their integer values
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    # Split the input string into a list of strings
    num_list: List[str] = numbers.split()

    # Sort the list of strings based on the dictionary values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list of strings back into a string with spaces in between
    sorted_str: str = ' '.join(sorted_num_list)

    return sorted_str