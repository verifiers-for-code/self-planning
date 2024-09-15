import math

def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    

 1. Create a function to round up each element in the list.
2. Square each element in the list.
3. Sum the squared elements.
4. Return the sum."""
    # Round up each element in the list
    lst = [math.ceil(x) for x in lst]
    # Square each element in the list
    lst = [x**2 for x in lst]
    # Sum the squared elements
    return sum(lst)