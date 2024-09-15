def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    

 1. Check if x and y are even.
2. If x is greater than y, return -1.
3. If x is even, return x.
4. If y is even, return y.
5. If x and y are both odd, return -1."""

    # Check if x and y are even
    if x % 2 == 0 and y % 2 == 0:
        # If x is greater than y, return -1
        if x > y:
            return -1
        # If x is even, return x
        elif x % 2 == 0:
            return x
        # If y is even, return y
        elif y % 2 == 0:
            return y
        # If x and y are both odd, return -1
        else:
            return -1
    else:
        return -1