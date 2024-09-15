def monotonic(l):
    if len(l) < 2:
        return True
    increasing = decreasing = True
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            decreasing = False
        elif l[i] < l[i-1]:
            increasing = False
    return increasing or decreasing