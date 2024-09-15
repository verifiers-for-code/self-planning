from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
    """
    separated_groups = []
    current_group = ''
    stack = []

    for char in paren_string:
        if char == '(':
            stack.append(char)
            current_group += char
        elif char == ')':
            if not stack:
                return "Error: Unbalanced parentheses"
            stack.pop()
            current_group += char
            if not stack:
                separated_groups.append(current_group)
                current_group = ''

    if stack:
        return "Error: Unbalanced parentheses"

    return separated_groups