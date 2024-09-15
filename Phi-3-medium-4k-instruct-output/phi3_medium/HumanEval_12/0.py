from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    # 1. Check if the list is empty.
    if not strings:
        return None

    # 2. Sort the list by length of strings.
    strings.sort(key=len)

    # 3. Return the last string in the sorted list.
    return strings[-1]