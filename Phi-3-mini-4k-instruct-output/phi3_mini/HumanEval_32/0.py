import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non-zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # Check if the list has an even number of coefficients
    if len(xs) % 2 != 0:
        raise ValueError("List of coefficients must have an even number of elements")

    # Check if the largest non-zero coefficient is positive
    if max(xs) <= 0:
        raise ValueError("Largest non-zero coefficient must be positive")

    # Use the Newton-Raphson method to find the zero of the polynomial
    x = 1.0  # Initial guess
    for _ in range(100):  # Maximum number of iterations
        fx = poly(xs, x)
        fpx = poly(xs, x, derivative=True)
        if abs(fx) < 1e-6:  # Convergence criterion
            return round(x, 2)
        x -= fx / fpx

    raise ValueError("Newton-Raphson method did not converge")


def poly_derivative(xs: list, x: float, derivative: bool = False):
    """
    Evaluates the derivative of a polynomial with coefficients xs at point x.
    If derivative is True, returns the derivative of the polynomial.
    """
    if derivative:
        return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i > 0])
    else:
        return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])