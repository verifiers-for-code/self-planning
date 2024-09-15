import re

def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    # Remove all non-alphanumeric characters and convert the string to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    
    # Compare the string with its reverse
    return cleaned_text == cleaned_text[::-1]