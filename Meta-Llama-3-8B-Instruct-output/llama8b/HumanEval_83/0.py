def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Calculate the total number of n-digit positive integers.
    total = 10 ** (n - 1) * 9

    # Calculate the number of n-digit positive integers that start with 1.
    start_with_one = 10 ** (n - 1)

    # Calculate the number of n-digit positive integers that end with 1.
    end_with_one = 10 ** (n - 1)

    # Calculate the number of n-digit positive integers that do not start with 1.
    not_start_with_one = total - start_with_one

    # Calculate the number of n-digit positive integers that do not end with 1.
    not_end_with_one = total - end_with_one

    # Add the number of n-digit positive integers that start with 1 and the number of n-digit positive integers that end with 1 to get the total count of the numbers of n-digit positive integers that start or end with 1.
    count = start_with_one + end_with_one

    return count