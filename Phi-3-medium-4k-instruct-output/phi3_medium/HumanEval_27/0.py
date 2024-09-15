def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # 1. Create an empty string to store the result.
    result = ""

    # 2. Loop through the string.
    for char in string:
        # 3. For each character, check if it is lowercase or uppercase.
        if char.islower():
            # 4. If it is lowercase, convert it to uppercase and add it to the result string.
            result += char.upper()
        elif char.isupper():
            # 5. If it is uppercase, convert it to lowercase and add it to the result string.
            result += char.lower()
        else:
            # If the character is neither lowercase nor uppercase, add it to the result string as is.
            result += char

    # 6. Return the result string.
    return result