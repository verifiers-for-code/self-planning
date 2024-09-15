def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize the result as infinity
    result = float('inf')
    # Initialize the current sum as 0
    current_sum = 0
    # Loop the input list
    for num in nums:
        # Add the current number to the current sum
        current_sum += num
        # If the current sum is less than the result, update the result
        if current_sum < result:
            result = current_sum
        # If the current sum is greater than 0, reset the current sum to the current number
        if current_sum > 0:
            current_sum = num
    # Return the result
    return result