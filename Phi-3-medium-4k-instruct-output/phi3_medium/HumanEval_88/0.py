def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]

    :param array: List of non-negative integers
    :return: Sorted list of integers
    """
    # Create a copy of the given array
    sorted_array = array.copy()

    # Check if the sum of the first and last index values is even or odd
    if (sorted_array[0] + sorted_array[-1]) % 2 == 0:
        # Sort the copied array in descending order if the sum is even
        sorted_array.sort(reverse=True)
    else:
        # Sort the copied array in ascending order if the sum is odd
        sorted_array.sort()

    return sorted_array