def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.
    
    Parameters:
    string (str): The original string to search in.
    substring (str): The substring to search for.
    
    Returns:
    int: The number of times the substring can be found in the original string.
    """
    count = 0
    start_index = 0
    
    while start_index < len(string):
        if string[start_index:start_index + len(substring)] == substring:
            count += 1
            start_index += 1
        else:
            start_index += 1
    
    return count