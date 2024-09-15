def derivative(xs: list):
    """Return the derivative of a polynomial represented by the coefficients in xs."""
    result = []  # Create an empty list to store the coefficients of the derivative.
    for i in range(1, len(xs)):  # Loop through the input list, starting from the second element (index 1).
        result.append(i * xs[i])  # For each element, multiply it by its index (plus 1) and add it to the result list.
    return result