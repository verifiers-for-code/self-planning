def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    # Convert the lists to sets
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets
    intersection = set1 & set2
    
    # Convert the intersection back to a list
    common_elements = list(intersection)
    
    # Sort the list
    common_elements.sort()
    
    return common_elements