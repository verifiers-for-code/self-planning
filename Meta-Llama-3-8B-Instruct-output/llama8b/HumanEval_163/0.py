def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Create an empty list to store the even digits
    even_digits = []

    # Loop from a to b (inclusive)
    for i in range(a, b + 1):
        # Check if the current number is even
        if i % 2 == 0:
            # If yes, add it to the list
            even_digits.append(i)

    # Return the list
    return even_digits