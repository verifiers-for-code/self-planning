def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Convert the number to a string
    number_str = str(number)

    # Split the string at the decimal point
    parts = number_str.split('.')

    # Return the second part of the split string
    return float(parts[1])