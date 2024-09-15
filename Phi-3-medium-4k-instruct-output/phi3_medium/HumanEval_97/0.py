def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    

 1. Extract the unit digits of both numbers.
2. Multiply the unit digits.
3. Return the product."""
    
    # Extract the unit digits of both numbers
    unit_digit_a = abs(a) % 10
    unit_digit_b = abs(b) % 10
    
    # Multiply the unit digits
    product = unit_digit_a * unit_digit_b
    
    # Return the product
    return product

# Test the function with the provided examples
print(multiply(148, 412)) # should return 16
print(multiply(19, 28)) # should return 72
print(multiply(2020, 1851)) # should return 0
print(multiply(14, -15)) # should return 20