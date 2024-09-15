def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    

 1. Convert the integer to a string.
2. Initialize even and odd counters to 0.
3. Loop through the string, if the digit is even, increment the even counter, else increment the odd counter.
4. Return a tuple of even and odd counters."""

    # Convert the integer to a string
    num_str = str(abs(num))

    # Initialize even and odd counters to 0
    even_count = 0
    odd_count = 0

    # Loop through the string
    for digit in num_str:
        # Check if the digit is even
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # Return a tuple of even and odd counters
    return (even_count, odd_count)