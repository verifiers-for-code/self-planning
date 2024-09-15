def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    

 1. Split the string by commas and spaces.
2. Return the resulting list."""
    # Split the string by commas and spaces
    words = s.replace(',', ' ').split()
    
    # Return the resulting list
    return words