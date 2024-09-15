def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    
    :param n: The upper limit of the sum
    :type n: int
    :return: The sum of numbers from 1 to n
    :rtype: int
    """
    # Use the formula for the sum of an arithmetic series: n*(n+1)/2
    result = n * (n + 1) // 2
    return result