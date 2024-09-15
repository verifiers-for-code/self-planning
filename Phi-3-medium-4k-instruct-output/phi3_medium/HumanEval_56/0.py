def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    # 1. Create a counter for opening and closing brackets.
    open_bracket_count = 0

    # 2. Loop through the string, increment the counter for opening brackets and decrement for closing brackets.
    for bracket in brackets:
        if bracket == "<":
            open_bracket_count += 1
        elif bracket == ">":
            open_bracket_count -= 1

        # 3. If the counter is negative at any point, return False.
        if open_bracket_count < 0:
            return False

    # 4. If the counter is not zero at the end, return False.
    if open_bracket_count != 0:
        return False

    # 5. Otherwise, return True.
    return True