from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    

 1. Check if the list is empty.
2. If not, find the longest string in the list.
3. Return the longest string."""
    if not strings:
        return None
    longest_string = strings[0]
    for string in strings[1:]:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string