from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # Split the input string by spaces to get a list of groups
    groups = paren_string.split()

    result = []

    for group in groups:
        # Initialize a counter and a stack
        counter = 0
        stack = []

        # Loop through the characters of the group
        for char in group:
            # If the character is '(', push it to the stack and increment the counter
            if char == '(':
                stack.append(char)
                counter += 1
            # If the character is ')', pop from the stack and decrement the counter
            elif char == ')':
                stack.pop()
                counter -= 1

        # The maximum value of the counter during the loop is the deepest level of nesting
        result.append(counter)

    # Return the result list
    return result