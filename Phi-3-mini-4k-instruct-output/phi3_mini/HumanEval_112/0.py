def is_palindrome(s):
    """Check if a string is palindrome."""
    return s == s[::-1]

def delete_chars(s, c):
    """Delete characters in s that are equal to any character in c."""
    return ''.join([char for char in s if char not in c])

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
    """
    result = delete_chars(s, c)
    return (result, is_palindrome(result))