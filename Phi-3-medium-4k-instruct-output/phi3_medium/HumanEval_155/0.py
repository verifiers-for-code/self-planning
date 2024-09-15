def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
    """
    # 1. Convert the number to its absolute value.
    num = abs(num)
    
    # 2. Convert the number to a string.
    num_str = str(num)
    
    # 3. Initialize even and odd counters to 0.
    even_count = 0
    odd_count = 0
    
    # 4. Loop through the string, increment the even counter if the digit is even, and increment the odd counter if the digit is odd.
    for digit in num_str:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    # 5. Return a tuple of the even and odd counters.
    return (even_count, odd_count)