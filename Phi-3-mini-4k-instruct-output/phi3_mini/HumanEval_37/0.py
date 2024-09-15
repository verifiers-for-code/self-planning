def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Step 1: Identify even indices
    even_indices = [i for i in range(len(l)) if i % 2 == 0]

    # Step 2: Sort even indices
    even_indices.sort()

    # Step 3: Create new list
    new_list = []
    for i in range(len(l)):
        if i in even_indices:
            # Replace value with corresponding value from sorted even indices
            new_list.append(l[even_indices[even_indices.index(i)]])
        else:
            # Keep original value
            new_list.append(l[i])

    return new_list