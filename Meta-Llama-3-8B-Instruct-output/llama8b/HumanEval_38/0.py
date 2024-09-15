def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    
    1. Split the string into groups of 3 characters.
    2. For each group, rotate the characters to the right by 1 position.
    3. Join the groups back together to form the decoded string.
    
    Note: The decode_cyclic function is the inverse of the encode_cyclic function.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # reverse the cycle in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)