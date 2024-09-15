def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Check if the given number is even
    if n % 2 != 0:
        return False

    # If the number is less than 8, return False
    if n < 8:
        return False

    # If the number is 8, return True
    if n == 8:
        return True

    # If the number is greater than 8, return True
    return True