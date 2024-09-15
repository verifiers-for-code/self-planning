def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    # 1. Create a list to store the number of stones in each level.
    pile = []

    # 2. Add the first level of stones to the list.
    pile.append(n)

    # 3. Loop from the second level to the nth level.
    for i in range(1, n):
        # 4. If n is odd, add the next odd number to the list.
        if n % 2 != 0:
            pile.append(pile[-1] + 2)
        # 5. If n is even, add the next even number to the list.
        else:
            pile.append(pile[-1] + 2)

    # 6. Return the list.
    return pile