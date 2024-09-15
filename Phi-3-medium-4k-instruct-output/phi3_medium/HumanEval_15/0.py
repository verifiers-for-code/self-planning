def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # Step 1: Create a list of numbers from 0 to n
    numbers = list(range(n + 1))
    
    # Step 2: Convert the list to a string with space-delimited numbers
    numbers_str = ' '.join(map(str, numbers))
    
    # Step 3: Return the string
    return numbers_str