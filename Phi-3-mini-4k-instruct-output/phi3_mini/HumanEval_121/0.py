def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    

 1. Create a list of odd elements in even positions.
2. Calculate the sum of the list.
3. Return the sum."""
    
    # Create a list of odd elements in even positions
    odd_even_positions = [lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 != 0]
    
    # Calculate the sum of the list
    sum_of_odd_even_positions = sum(odd_even_positions)
    
    # Return the sum
    return sum_of_odd_even_positions