def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """
    new_str = ""
    for char in s:
        if char.isalpha():
            if char.islower():
                new_str += char.upper()
            else:
                new_str += char.lower()
        else:
            new_str += char
    if not any(char.isalpha() for char in s):
        return s[::-1]
    return new_str