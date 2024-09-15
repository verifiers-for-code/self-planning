from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    

 1. Use the join() method to concatenate the list of strings into a single string.
2. Return the concatenated string."""
    return ''.join(strings)