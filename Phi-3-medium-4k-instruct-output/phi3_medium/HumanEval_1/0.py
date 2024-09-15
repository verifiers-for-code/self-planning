from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
    :param paren_string: A string containing multiple groups of nested parentheses
    :return: A list of strings, each string representing a separate group of balanced parentheses
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Create a stack to keep track of the opening parentheses
    stack = []

    # Create a list to store the groups of balanced parentheses
    groups = []

    # Iterate through the string
    for char in paren_string:
        if char == "(":
            # If it's an opening parenthesis, push it to the stack
            stack.append(char)
        elif char == ")":
            # If it's a closing parenthesis, pop from the stack and add the popped opening parenthesis to the current group
            if stack:
                group = stack.pop() + char
                if not groups:
                    groups.append(group)
                else:
                    groups[-1] += group
            else:
                # If the stack is empty and we encounter a closing parenthesis, the input string is not balanced
                return []

    # If the stack is not empty after the iteration, return an empty list as the input string is not balanced
    if stack:
        return []

    # Return the list of groups
    return groups