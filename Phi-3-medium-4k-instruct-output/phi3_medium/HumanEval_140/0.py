def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    

 1. Replace all spaces with underscores.
2. Replace all occurrences of more than two consecutive underscores with a single hyphen.
3. Return the modified string."""
    
    # Replace all spaces with underscores
    text = text.replace(" ", "_")
    
    # Replace all occurrences of more than two consecutive underscores with a single hyphen
    while "__" in text:
        text = text.replace("__", "_")
    while "___" in text:
        text = text.replace("___", "-")
    
    return text