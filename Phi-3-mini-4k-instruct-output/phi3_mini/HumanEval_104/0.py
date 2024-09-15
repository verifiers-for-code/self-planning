def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    

 1. Create a function to check if a number has even digits.
2. Loop the input list, if the number has no even digits, add it to the result list.
3. Sort the result list.
4. Return the result list."""

    def has_even_digit(n):
        """Check if a number has even digits."""
        for digit in str(n):
            if int(digit) % 2 == 0:
                return True
        return False

    result = []
    for num in x:
        if not has_even_digit(num):
            result.append(num)

    result.sort()
    return result