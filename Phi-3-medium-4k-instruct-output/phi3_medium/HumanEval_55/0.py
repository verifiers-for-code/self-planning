def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    
    :param n: The n-th Fibonacci number to calculate
    :type n: int
    :return: The n-th Fibonacci number
    :rtype: int
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)