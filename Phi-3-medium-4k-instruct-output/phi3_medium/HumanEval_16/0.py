def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # 1. Convert the string to lowercase.
    string = string.lower()

    # 2. Create a set of characters from the string.
    char_set = set(string)

    # 3. Return the length of the set.
    return len(char_set)