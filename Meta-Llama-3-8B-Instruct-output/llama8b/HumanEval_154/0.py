def cycpattern_check(a, b):
    b_set = set(b)
    for i in range(len(a) - len(b) + 1):
        if set(a[i:i+len(b)]) == b_set or set(a[i:i+len(b)][1:] + a[i:i+len(b)][0]) == b_set:
            return True
    return False