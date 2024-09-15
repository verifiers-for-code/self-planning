def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]
    """

    # Create a function to count the number of ones in the binary representation of a number.
    def count_ones(n):
        return bin(n).count('1')

    # Sort the input array using the count of ones in the binary representation as the primary key, and the decimal value as the secondary key.
    arr.sort(key=lambda x: (count_ones(x), x))

    # Return the sorted array.
    return arr