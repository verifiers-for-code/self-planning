def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
    """
    # 1. Check if x is greater than y, if so, return -1.
    if x > y:
        return -1

    # 2. If x is even, set x as the result.
    if x % 2 == 0:
        result = x
    # 3. If x is odd, set x as x + 1.
    else:
        result = x + 1

    # 4. Loop from x to y, if the number is even, set it as the result.
    for i in range(x, y + 1):
        if i % 2 == 0:
            result = i

    # 5. Return the result.
    return result