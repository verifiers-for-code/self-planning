def multiply(a, b):
    # Calculate the unit digits of the two numbers
    unit_digit_a = a % 10
    unit_digit_b = b % 10
    
    # Multiply the unit digits together
    product = unit_digit_a * unit_digit_b
    
    # Return the result
    return product