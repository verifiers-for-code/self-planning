def order_by_points(nums):
    return [x for _, x in sorted((sum(int(digit) for digit in str(abs(num))), i, num) for i, num in enumerate(nums))]