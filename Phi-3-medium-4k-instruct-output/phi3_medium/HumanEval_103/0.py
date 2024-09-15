def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    
    Parameters:
    n (int): The first integer
    m (int): The second integer
    
    Returns:
    str: The binary representation of the rounded average of the integers from n through m
    """
    # Check if n is greater than m
    if n > m:
        return -1
    
    # Compute the average of the integers from n through m
    avg = sum(range(n, m+1)) / (m-n+1)
    
    # Round the average to the nearest integer
    rounded_avg = round(avg)
    
    # Convert the rounded average to binary
    binary_avg = bin(rounded_avg)
    
    # Return the binary representation
    return binary_avg