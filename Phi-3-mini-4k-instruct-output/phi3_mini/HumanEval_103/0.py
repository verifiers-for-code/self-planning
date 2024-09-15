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
    

 1. Check if n is greater than m, return -1.
2. Calculate the sum of integers from n to m.
3. Calculate the average of the integers.
4. Round the average to the nearest integer.
5. Convert the rounded average to binary.
6. Return the binary representation."""
    if n > m:
        return -1
    else:
        total_sum = sum(range(n, m+1))
        avg = total_sum / (m - n + 1)
        rounded_avg = round(avg)
        binary_avg = bin(rounded_avg)
        return binary_avg