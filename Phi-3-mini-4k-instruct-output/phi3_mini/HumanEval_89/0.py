def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    
    1. Create a list of all the letters in the alphabet.
    2. Create a variable to store the result.
    3. Loop through the input string.
    4. For each character, find its index in the alphabet list.
    5. Add two to the index and take the modulus of 26 to handle the wrap-around.
    6. Add the new character to the result string.
    7. Return the result string."""
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for char in s:
        index = (alphabet.index(char) + 2) % 26
        result += alphabet[index]
    return result