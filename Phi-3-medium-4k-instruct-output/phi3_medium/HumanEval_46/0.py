def fib4(n: int) -> int:
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    # Create a list to store the first four numbers of the sequence
    fib_list = [0, 0, 2, 0]

    # Loop from 4 to n
    for i in range(4, n + 1):
        # Calculate the next number in the sequence by adding the last four numbers in the list
        next_num = fib_list[i - 1] + fib_list[i - 2] + fib_list[i - 3] + fib_list[i - 4]

        # Append the next number to the list
        fib_list.append(next_num)

    # Return the n-th number in the list
    return fib_list[n]