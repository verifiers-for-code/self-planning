def iscube(a):
    """
    This function checks if a given integer is a cube of some integer number.
    
    Parameters:
    a (int): The input integer to be checked.
    
    Returns:
    bool: True if the integer is a cube, False otherwise.
    """
    # Calculate the cube root of the input number
    cube_root = round(a ** (1. / 3))
    
    # Check if the cube root is an integer
    if cube_root ** 3 == a:
        return True
    else:
        return False