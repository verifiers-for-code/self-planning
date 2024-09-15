from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    # Create an empty list for the result
    result = []

    # Loop through the input list of strings
    for string in strings:
        # If the current string contains the given substring, append it to the result list
        if substring in string:
            result.append(string)

    # Return the result list
    return result