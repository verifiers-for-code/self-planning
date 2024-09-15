def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    rev_string = string[::-1]
    for i in range(len(string)):
        if is_palindrome(string[:i+1]):
            return string + rev_string[i:]
    return string + rev_string