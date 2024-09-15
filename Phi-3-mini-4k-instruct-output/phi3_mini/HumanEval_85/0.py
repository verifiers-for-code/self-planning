def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..

    Examples:
        add([4, 2, 6, 7]) ==> 2 

    1. Create a list of even elements at odd indices.
    2. Sum the elements in the list.
    3. Return the sum."""
    # Create a list of even elements at odd indices
    even_odd_indices = [lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0]
    # Sum the elements in the list
    sum_even_odd_indices = sum(even_odd_indices)
    # Return the sum
    return sum_even_odd_indices