from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    level = 0
    stack = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
            level += 1
        elif char == ')':
            stack.pop()
            level -= 1
        if not stack:
            result.append(level)
    return result