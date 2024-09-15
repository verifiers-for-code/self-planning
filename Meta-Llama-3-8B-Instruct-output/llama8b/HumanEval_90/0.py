def next_smallest(lst):
    if not lst:
        return None
    sorted_lst = sorted(lst)
    if len(sorted_lst) < 2:
        return None
    return sorted_lst[1]