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
    def sum_of_digits(num):
        """
        Calculate the sum of digits of a number.
        """
        return sum(int(digit) for digit in str(abs(num)))

    # Create a list of tuples, where each tuple contains the original index and the sum of digits.
    indexed_nums = [(i, sum_of_digits(num)) for i, num in enumerate(nums)]

    # Sort the list of tuples based on the sum of digits and index.
    sorted_indexed_nums = sorted(indexed_nums, key=lambda x: (x[1], x[0]))

    # Return a list of the original numbers in the sorted order.
    return [num for i, num in sorted_indexed_nums]