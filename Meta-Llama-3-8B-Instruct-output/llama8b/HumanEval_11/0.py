from typing import List

def string_xor(a: str, b: str) -> str:
    """Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
    1. Initialize an empty string result.
    2. Loop through the characters of the input strings.
    3. For each pair of characters, perform a binary XOR operation and append the result to the result string.
    4. Return the result string."""
    result = ''
    for char_a, char_b in zip(a, b):
        result += str(int(char_a) ^ int(char_b))
    return result