def solve(s):
    result = ""
    for char in s:
        if char.isalpha():
            result += char.swapcase()
        else:
            if result:
                result = result[::-1]
            result += char
    if result:
        result = result[::-1]
    return result