def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Step 1: Create a list of all the even indices of the given list
    even_indices = [i for i in range(len(l)) if i % 2 == 0]

    # Step 2: Sort the list of even indices
    sorted_even_indices = sorted(even_indices, key=lambda i: l[i])

    # Step 3: Return a new list that is identical to the original list in the odd indicies, and equal to the sorted even indices in the even indicies
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(l[sorted_even_indices.pop(0)])
        else:
            result.append(l[i])
    return result