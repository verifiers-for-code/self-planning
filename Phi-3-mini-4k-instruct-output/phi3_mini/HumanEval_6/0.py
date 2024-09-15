from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Split the input string by spaces to get the groups
    groups = paren_string.split()

    # Initialize an empty list to store the results
    result = []

    # Loop through each group
    for group in groups:
        # Initialize a counter to 0
        counter = 0

        # Loop through the characters in the group
        for char in group:
            # If the character is '(', increment the counter
            if char == '(':
                counter += 1
            # If the character is ')', decrement the counter
            elif char == ')':
                counter -= 1

            # If the counter is greater than the current maximum, update the maximum
            if counter > result[-1]:
                result.append(counter)

    # Return the result list
    return result