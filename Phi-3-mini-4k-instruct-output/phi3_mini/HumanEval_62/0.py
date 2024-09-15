def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Create a list to store the derivative coefficients
    derivative_coefficients = []

    # Loop the input list, calculate the derivative coefficient for each term
    for i in range(len(xs) - 1):
        derivative_coefficients.append(xs[i] * (len(xs) - i - 1))

    # Return the derivative coefficients list
    return derivative_coefficients