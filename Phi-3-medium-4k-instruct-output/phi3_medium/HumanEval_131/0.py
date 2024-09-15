def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # 1. Convert the integer to a string.
    n_str = str(n)
    
    # 2. Initialize a variable to store the product of the odd digits.
    product = 1
    
    # 3. Loop through the string, if the digit is odd, multiply it with the product variable.
    for digit in n_str:
        if int(digit) % 2 != 0:
            product *= int(digit)
    
    # 4. If the product variable is still 1 after the loop, return 0.
    if product == 1:
        return 0
    
    # 5. Return the product variable.
    return product