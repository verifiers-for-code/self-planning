def swap_case(message):
    """
    This function swaps the case of all letters in the message.
    """
    return message.swapcase()

def replace_vowels(message):
    """
    This function replaces all vowels in the message with the letter that appears 2 places ahead of that vowel in the english alphabet.
    """
    vowels = 'aeiouAEIOU'
    result = ''
    for char in message:
        if char in vowels:
            index = vowels.index(char)
            if index + 2 < len(vowels):
                result += vowels[index + 2]
            else:
                result += vowels[0]
        else:
            result += char
    return result

def encode(message):
    """
    This function combines the two functions to create the final encoded message.
    """
    return replace_vowels(swap_case(message))