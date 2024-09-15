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
    
    """
    # 1. Check if the array is empty, return None if it is.
    if not arr:
        return None

    # 2. Calculate the product of all signs in the array.
    sign_product = 1
    for num in arr:
        if num > 0:
            sign_product *= 1
        elif num < 0:
            sign_product *= -1

    # 3. Calculate the sum of the magnitudes of all integers in the array.
    magnitude_sum = sum(abs(num) for num in arr)

    # 4. Multiply the product of signs with the sum of magnitudes.
    result = sign_product * magnitude_sum

    # 5. Return the result.
    return result