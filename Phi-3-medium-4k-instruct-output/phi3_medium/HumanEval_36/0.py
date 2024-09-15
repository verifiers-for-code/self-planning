def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # 1. Create a counter.
    count = 0
    
    # 2. Loop from 1 to n-1.
    for i in range(1, n):
        # 3. Check if the number is divisible by 11 or 13.
        if i % 11 == 0 or i % 13 == 0:
            # 4. If yes, count the number of 7s in the number.
            count += str(i).count('7')
    
    # 5. Return the counter.
    return count