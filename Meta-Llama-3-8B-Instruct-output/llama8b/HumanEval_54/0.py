def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    
    Args:
    s0 (str): The first string.
    s1 (str): The second string.
    
    Returns:
    bool: True if the strings have the same characters, False otherwise.
    """
    return set(s0) == set(s1)