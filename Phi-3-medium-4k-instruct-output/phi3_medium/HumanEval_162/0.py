import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    # Check if the input string is empty
    if not text:
        return None

    # Use the hashlib library to generate the md5 hash of the string
    md5_hash = hashlib.md5(text.encode())

    # Return the hexadecimal representation of the hash
    return md5_hash.hexdigest()