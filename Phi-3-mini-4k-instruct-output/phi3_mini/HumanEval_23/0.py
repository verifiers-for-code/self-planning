def strlen(string: str) -> int:
    """ Return Return the length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)


def check_if_last_char_is_a_letter(txt: str) -> bool:
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") → False
    check_if_last_char_is_a_letter("apple pi e") → True
    check_if_last_char_is_a_letter("apple pi e ") → False
    check_if_last_char_is_a_letter("") → False
    """
    if not txt:
        return False
    if not txt[-1].isalpha():
        return False
    if txt[-1] == ' ':
        return False
    if txt[-1] == '.' or txt[-1] == ',' or txt[-1] == '!' or txt[-1] == '?':
        return False
    if txt[-1] == ' ' and len(txt) > 1:
        return False
    if txt[-1] == '.' and len(txt) > 1:
        return False
    if txt[-1] == ',' and len(txt) > 1:
        return False
    if txt[-1] == '!' and len(txt) > 1:
        return False
    if txt[-1] == '?' and len(txt) > 1:
        return False
    return True


def encrypt(s: str) -> str:
    """
    Create a function that takes a string and returns a string that is encrypted by shifting the alphabet by the alphabet alphabetically rotated by two places down and two places to the right.

    Examples:
    encrypt('abc') → 'ghi'
    encrypt('ghi') → 'cde'
    encrypt('xyz') → 'vwx'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[2:] + alphabet[:2]
    encrypted = ''
    for char in s:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted += shifted_alphabet[index]
        else:
            encrypted += char
    return encrypted