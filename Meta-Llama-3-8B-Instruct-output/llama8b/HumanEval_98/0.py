def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0  # Initialize a counter variable to 0
    for i in range(0, len(s), 2):  # Loop through the string, considering only even indices
        char = s[i]  # Get the character at the current index
        if char in 'AEIOU':  # Check if the character is an uppercase vowel
            count += 1  # If it is, increment the counter
    return count  # Return the counter