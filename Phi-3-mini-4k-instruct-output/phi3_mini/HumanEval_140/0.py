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
2. Loop the string, if more than 2 consecutive spaces, replace with -.
3. Return the modified string."""
    
    # Step 1: Replace all spaces with underscores
    text = text.replace(' ', '_')
    
    # Step 2: Loop the string, if more than 2 consecutive spaces, replace with -
    i = 0
    while i < len(text) - 2:
        if text[i] == '_' and text[i+1] == '_' and text[i+2] == '_':
            text = text[:i+1] + '-' + text[i+3:]
        i += 1
    
    # Step 3: Return the modified string
    return text