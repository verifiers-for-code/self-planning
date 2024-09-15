def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
    :param s: input string
    :return: number of uppercase vowels in even indices
    """
    vowels = ['A', 'E', 'I', 'O', 'U']
    even_indices = [i for i in range(len(s)) if i % 2 == 0]
    count = 0
    for i in even_indices:
        if s[i] in vowels and s[i].isupper():
            count += 1
    return count