def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    

 1. Create a function to check if the given number can be written as the sum of exactly 4 positive even numbers.
2. Loop the given number from 2 to n.
3. Check if the given number can be written as the sum of exactly 4 positive even numbers.
4. Return True or False."""
    for i in range(2, n+1):
        if i % 2 == 0:
            for j in range(2, n+1):
                if j % 2 == 0:
                    for k in range(2, n+1):
                        if k % 2 == 0:
                            for l in range(2, n+1):
                                if l % 2 == 0:
                                    if i + j + k + l == n:
                                        return True
    return False