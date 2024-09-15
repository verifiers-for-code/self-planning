def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices.


    Examples:
        add([4, 2, 6, 7]) ==> 2 

    """
    # 1. Create a variable to store the sum of even numbers at odd indices.
    sum_even_odd_indices = 0

    # 2. Loop through the list, check if the index is odd and the number is even.
    for i in range(len(lst)):
        if i % 2 != 0 and lst[i] % 2 == 0:
            # 3. If both conditions are met, add the number to the sum.
            sum_even_odd_indices += lst[i]

    # 4. Return the sum.
    return sum_even_odd_indices