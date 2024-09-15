def swap_case(message):
    """
    Swap the case of all letters in the message.
    """
    return ''.join([char.lower() if char.isupper() else char.upper() for char in message])

def replace_vowels(message):
    """
    Replace all vowels in the message with the letter that appears 2 places ahead of that vowel in the english alphabet.
    """
    vowels = 'aeiou'
    new_message = ''
    for char in message:
        if char.lower() in vowels:
            new_char = chr(ord(char) + 2)
            if new_char > 'u':
                new_char = chr(ord(new_char) - 26)
            new_message += new_char
        else:
            new_message += char
    return new_message

def encode(message):
    """
    Encode the message by swapping case of all letters, and replacing all vowels with the letter that appears 2 places ahead of that vowel in the english alphabet.
    """
    swapped_case = swap_case(message)
    encoded_message = replace_vowels(swapped_case)
    return encoded_message