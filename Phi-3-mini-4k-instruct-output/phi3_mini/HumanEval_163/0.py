def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    

    1. Create a list of even digits between a and b.
    2. Return the list."""
    
    # Create a list of even digits between a and b
    even_digits = [str(i) for i in range(a, b+1) if i % 2 == 0]
    
    # Convert the list of strings to a list of integers
    even_digits = [int(digit) for digit in even_digits]
    
    # Return the list of even digits
    return even_digits