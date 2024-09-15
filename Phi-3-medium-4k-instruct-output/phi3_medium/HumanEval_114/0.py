def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # 1. Initialize the current sum and the minimum sum to the first element of the array.
    current_sum = min_sum = nums[0]
    
    # 2. Loop through the array starting from the second element.
    for num in nums[1:]:
        # 3. Update the current sum by adding the current element.
        current_sum += num
        
        # 4. If the current sum is less than the current element, update the current sum to the current element.
        current_sum = min(current_sum, num)
        
        # 5. If the current sum is less than the minimum sum, update the minimum sum to the current sum.
        min_sum = min(min_sum, current_sum)
    
    # 6. Return the minimum sum.
    return min_sum