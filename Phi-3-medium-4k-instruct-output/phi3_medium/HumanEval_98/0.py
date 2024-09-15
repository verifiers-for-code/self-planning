def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # 1. Create a list of uppercase vowels.
    upper_vowels = ['A', 'E', 'I', 'O', 'U']
    
    # Initialize count to 0
    count = 0
    
    # 2. Loop through the string, check if the character is an uppercase vowel and its index is even.
    for i in range(len(s)):
        if i % 2 == 0 and s[i] in upper_vowels:
            # 3. If yes, increment the count.
            count += 1
            
    # 4. Return the count.
    return count