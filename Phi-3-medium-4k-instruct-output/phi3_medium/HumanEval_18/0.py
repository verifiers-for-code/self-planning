def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # Step 1: Use the built-in count method to count the number of non-overlapping occurrences of the substring in the string.
    non_overlapping_count = string.count(substring)

    # Step 2: Subtract the length of the substring from the length of the string.
    string_length_minus_substring_length = len(string) - len(substring)

    # Step 3: Divide the result by the length of the substring.
    overlapping_count = string_length_minus_substring_length // len(substring)

    # Step 4: Add the result of step 1 to the result of step 3.
    total_count = non_overlapping_count + overlapping_count

    # Step 5: Return the result.
    return total_count