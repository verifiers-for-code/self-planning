def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    

    :param lst: List of integers
    :type lst: list
    :return: Sum of all odd elements in even positions
    :rtype: int
    """
    # 1. Create a variable to store the sum of odd elements in even positions.
    sum_odd_even = 0

    # 2. Loop through the list with index.
    for i, num in enumerate(lst):
        # 3. Check if the index is even and the element is odd.
        if i % 2 == 0 and num % 2 != 0:
            # 4. If both conditions are met, add the element to the sum.
            sum_odd_even += num

    # 5. Return the sum.
    return sum_odd_even