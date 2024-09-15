def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. Assume only letters.
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    # 1. Create a dictionary to map vowels to the letter that appears 2 places ahead of that vowel in the english alphabet.
    vowel_map = {
        'a': 'c',
        'e': 'g',
        'i': 'k',
        'o': 'q',
        'u': 'w'
    }
    
    # 2. Create a new string.
    encoded_message = ""
    
    # 3. Loop through the message, for each character:
    for char in message:
        # If it's a vowel, replace it with the corresponding letter from the dictionary.
        if char.lower() in vowel_map:
            encoded_message += vowel_map[char.lower()].upper() if char.isupper() else vowel_map[char.lower()]
        # If it's a letter, swap its case.
        elif char.isalpha():
            encoded_message += char.swapcase()
        # If it's not a letter, leave it as it is.
        else:
            encoded_message += char
    
    # 4. Return the new string.
    return encoded_message