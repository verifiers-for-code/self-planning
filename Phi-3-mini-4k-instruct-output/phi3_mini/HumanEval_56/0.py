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
    

 1. Create a stack.
2. Loop the input string.
3. If the character is "<", push it to the stack.
4. If the character is ">", pop the stack.
5. If the stack is empty, return False.
6. Return True if the stack is empty after the loop."""
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if not stack:
                return False
            stack.pop()
    return not stack