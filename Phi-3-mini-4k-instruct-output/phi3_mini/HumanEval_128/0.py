def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    

 1. If the array is empty, return None.
2. Initialize a variable to store the product of signs.
3. Loop through the array, if the number is not zero, multiply the product of signs by the sign of the number.
4. Calculate the sum of magnitudes of integers multiplied by the product of signs.
5. Return the result."""
    if not arr:
        return None
    product_of_signs = 1
    for num in arr:
        if num != 0:
            product_of_signs *= (-1 if num < 0 else 1)
    return sum(abs(num) * product_of_signs for num in arr)