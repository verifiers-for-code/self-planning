def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    # Step 1: Create a list of tuples, where each tuple contains the original number and the sum of its digits.
    nums_with_sums = [(num, sum(int(digit) for digit in str(abs(num)))) for num in nums]

    # Step 2: Sort the list of tuples based on the sum of digits, and then based on the original index.
    nums_with_sums.sort(key=lambda x: (x[1], nums.index(x[0])))

    # Step 3: Extract the sorted numbers from the list of tuples.
    sorted_nums = [num for num, _ in nums_with_sums]

    # Step 4: Return the sorted list of numbers.
    return sorted_nums