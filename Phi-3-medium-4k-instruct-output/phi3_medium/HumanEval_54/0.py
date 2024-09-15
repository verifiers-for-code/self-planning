def same_chars(s0: str, s1: str) -> bool:
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
    
    :param s0: First string
    :param s1: Second string
    :return: True if both strings have the same characters, False otherwise
    """
    # Create frequency dicts for both strings
    freq_dict_s0 = {}
    freq_dict_s1 = {}
    
    for char in s0:
        if char in freq_dict_s0:
            freq_dict_s0[char] += 1
        else:
            freq_dict_s0[char] = 1
            
    for char in s1:
        if char in freq_dict_s1:
            freq_dict_s1[char] += 1
        else:
            freq_dict_s1[char] = 1
            
    # Compare the frequency dicts
    return freq_dict_s0 == freq_dict_s1