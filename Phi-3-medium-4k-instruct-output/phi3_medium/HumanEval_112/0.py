def reverse_delete(s, c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    
    1. Create a new string that contains all characters in s that are not in c.
    2. Check if the new string is a palindrome.
    3. Return a tuple containing the new string and the result of the palindrome check."""
    
    # Step 1: Create a new string that contains all characters in s that are not in c
    new_string = ''.join([char for char in s if char not in c])
    
    # Step 2: Check if the new string is a palindrome
    is_palindrome = new_string == new_string[::-1]
    
    # Step 3: Return a tuple containing the new string and the result of the palindrome check
    return (new_string, is_palindrome)