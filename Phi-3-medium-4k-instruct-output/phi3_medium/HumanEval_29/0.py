from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    # 1. Create an empty list to store the filtered strings.
    filtered_strings = []

    # 2. Loop through the input list of strings.
    for string in strings:
        # 3. Check if the current string starts with the given prefix.
        if string.startswith(prefix):
            # 4. If it does, append it to the filtered list.
            filtered_strings.append(string)

    # 5. Return the filtered list.
    return filtered_strings