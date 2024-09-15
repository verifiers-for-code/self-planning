def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # 1. Create a list to store the derivative coefficients.
    derivative_coeffs = []

    # 2. Loop through the input list, starting from the second element.
    for i in range(1, len(xs)):
        # 3. Multiply each element by its index and append to the derivative list.
        derivative_coeffs.append(xs[i] * i)

    # 4. Return the derivative list.
    return derivative_coeffs