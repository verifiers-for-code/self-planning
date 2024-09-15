def count_distinct_characters(string: str) -> int:
    """Given a string, find out how many distinct characters (regardless of case) does it consist of"""
    # Convert the string to lowercase
    string = string.lower()
    
    # Create a set to store unique characters
    distinct_chars = set()
    
    # Loop through the string, add each character to the set
    for char in string:
        distinct_chars.add(char)
    
    # Return the size of the set
    return len(distinct_chars)