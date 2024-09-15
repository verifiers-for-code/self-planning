def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    # Sort the sides in ascending order
    sides = sorted([a, b, c])
    
    # Check if the triangle inequality theorem holds
    if sides[0] + sides[1] <= sides[2]:
        return False
    
    # Check if the triangle is right-angled
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False