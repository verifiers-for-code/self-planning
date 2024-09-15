def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    
    Args:
        n (int): The number of cars in each direction.

    Returns:
        int: The number of collisions.
    """
    # Create a list of n integers, where each integer represents the position of a car.
    left_to_right = list(range(1, n+1))
    # Create a list of n integers, where each integer represents the position of a car moving in the opposite direction.
    right_to_left = list(range(n, 0, -1))

    # Sort both lists.
    left_to_right.sort()
    right_to_left.sort()

    # Initialize a counter for collisions.
    collisions = 0

    # Loop through both lists simultaneously, and count the number of collisions.
    for i in range(n):
        if left_to_right[i] == right_to_left[i]:
            collisions += 1

    # Return the number of collisions.
    return collisions