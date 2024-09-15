def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
    # Check if the string is empty
    if not txt:
        return False

    # Get the last character of the string
    last_char = txt[-1]

    # Check if the last character is an alphabetical character
    if not last_char.isalpha():
        return False

    # Check if the last character is not a part of a word
    words = txt.split()
    if len(words) > 1 and last_char == words[-1][-1]:
        return False

    return True