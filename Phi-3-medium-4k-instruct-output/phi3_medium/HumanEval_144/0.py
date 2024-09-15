def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    

 1. Convert the fractions to float.
2. Multiply the fractions.
3. Check if the result is a whole number.
4. Return True if the result is a whole number, False otherwise."""

    # Step 1: Convert the fractions to float
    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))
    x_float = x_num / x_denom
    n_float = n_num / n_denom

    # Step 2: Multiply the fractions
    result = x_float * n_float

    # Step 3: Check if the result is a whole number
    if result.is_integer():
        return True
    else:
        return False