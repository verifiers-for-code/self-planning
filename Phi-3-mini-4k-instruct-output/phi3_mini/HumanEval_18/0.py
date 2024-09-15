def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    index = 0
    while index < len(string):
        found_index = string.find(substring, index)
        if found_index == -1:
            break
        count += 1
        index = found_index + 1
    return count