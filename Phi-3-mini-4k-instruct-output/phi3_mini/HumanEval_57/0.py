def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    

 1. Check if the list is empty or has only one element.
2. If the list has more than one element, check if the list is monotonically increasing or decreasing.
3. Return True if the list is monotonically increasing or decreasing, otherwise return False.
4. If the list is empty or has only one element, return True."""
    if len(l) < 2:
        return True
    else:
        increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
        decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
        return increasing or decreasing