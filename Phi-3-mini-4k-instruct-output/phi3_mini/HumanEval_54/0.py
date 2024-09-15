def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    # Create a frequency dict for both strings
    freq_dict0 = {}
    freq_dict1 = {}
    for char in s0:
        if char in freq_dict0:
            freq_dict0[char] += 1
        else:
            freq_dict0[char] = 1
    for char in s1:
        if char in freq_dict1:
            freq_dict1[char] += 1
        else:
            freq_dict1[char] = 1

    # Compare the frequency dicts
    if freq_dict0 == freq_dict1:
        return True
    else:
        return False