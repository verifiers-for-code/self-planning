def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    
    :param n: non-negative integer
    :return: list of the first n + 1 numbers of the Tribonacci sequence
    """
    # Create a list to store the Tribonacci sequence
    tribonacci_sequence = [1, 3, 2]
    
    # Loop from 3 to n + 1
    for i in range(3, n + 1):
        # If the current number is even, add 1 + (current number / 2) to the list
        if i % 2 == 0:
            tribonacci_sequence.append(1 + (i // 2))
        # If the current number is odd, add the sum of the last three numbers in the list to the list
        else:
            tribonacci_sequence.append(tribonacci_sequence[-1] + tribonacci_sequence[-2] + tribonacci_sequence[-3])
    
    # Return the list
    return tribonacci_sequence