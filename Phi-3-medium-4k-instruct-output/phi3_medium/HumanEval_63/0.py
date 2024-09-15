def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    
    :param n: The n-th element of the fibfib sequence to compute
    :type n: int
    :return: The n-th element of the fibfib sequence
    :rtype: int
    """
    # Create a list to store the first three numbers of the sequence
    fibfib_sequence = [0, 0, 1]

    # Use a loop to calculate the next numbers in the sequence
    for i in range(3, n + 1):
        fibfib_sequence.append(fibfib_sequence[i - 1] + fibfib_sequence[i - 2] + fibfib_sequence[i - 3])

    # Return the n-th number in the sequence
    return fibfib_sequence[n]