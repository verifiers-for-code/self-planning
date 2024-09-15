def largest_smallest_integers(lst):
    negative = [x for x in lst if x < 0]
    positive = [x for x in lst if x > 0]
    
    if not negative and not positive:
        return None, None
    elif not negative:
        return None, min(positive)
    elif not positive:
        return max(negative), None
    else:
        return max(negative), min(positive)