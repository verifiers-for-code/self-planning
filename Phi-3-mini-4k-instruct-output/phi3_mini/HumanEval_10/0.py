def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome 

 1. Find the longest palindromic suffix of the string.
2. Reverse the prefix of the string that comes before the palindromic suffix.
3. Concatenate the reversed prefix and the original string to form the palindrome.
4. Return the palindrome."""
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if string == '':
        return ''
    for i in range(len(string), 0, -1):
        if is_palindrome(string[-i:]):
            return string + string[:-i][::-1]