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
    """
    # Create a list with the first two numbers of the Tribonacci sequence
    tribonacci = [1, 3]
    
    # Loop from 2 to n
    for i in range(2, n + 1):
        # If the index is even, calculate the next number using the formula
        if i % 2 == 0:
            next_num = 1 + i / 2
        # If the index is odd, calculate the next number using the recurrence relation
        else:
            next_num = tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i + 1]
        
        # Append the next number to the list
        tribonacci.append(next_num)
    
    # Return the list
    return tribonacci