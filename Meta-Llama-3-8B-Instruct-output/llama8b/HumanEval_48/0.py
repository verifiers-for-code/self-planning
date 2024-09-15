def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    """
    # Remove all non-alphanumeric characters from the string
    text = ''.join(e for e in text if e.isalnum())
    
    # Convert the string to lowercase
    text = text.lower()
    
    # Compare the string with its reverse
    return text == text[::-1]