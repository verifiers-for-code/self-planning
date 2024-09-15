import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    """
    if len(xs) % 2 != 0:
        return None
    def poly_prime(xs: list, x: float):
        """
        Evaluates derivative of polynomial with coefficients xs at point x.
        return derivative of xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
        """
        return sum([i * coeff * math.pow(x, i-1) for i, coeff in enumerate(xs)])
    def newton_raphson(x0: float, tol: float = 1e-5, max_iter: int = 100):
        """
        Use the Newton-Raphson method to find the root.
        """
        for _ in range(max_iter):
            x1 = x0 - poly(xs, x0) / poly_prime(xs, x0)
            if abs(x1 - x0) < tol:
                return round(x1, 2)
            x0 = x1
        return None
    return newton_raphson(max([abs(coeff) for coeff in xs]) / 2)