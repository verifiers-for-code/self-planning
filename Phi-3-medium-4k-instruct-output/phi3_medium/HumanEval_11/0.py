from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert the strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)

    # Perform XOR operation on the integers
    xor_result = int_a ^ int_b

    # Convert the result back to a string
    result = bin(xor_result)[2:]

    # Return the result
    return result