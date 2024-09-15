def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
    :param nums: List of integers
    :return: Count of numbers that meet the criteria
    """
    count = 0
    for num in nums:
        # Check if the number is greater than 10
        if num > 10:
            # Convert the number to a string to access the first and last digits
            num_str = str(num)
            # Check if the first and last digits are odd
            if int(num_str[0]) % 2 != 0 and int(num_str[-1]) % 2 != 0:
                count += 1
    return count