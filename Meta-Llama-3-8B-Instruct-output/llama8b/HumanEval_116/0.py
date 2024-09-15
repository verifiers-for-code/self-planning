def sort_array(arr):
    # Convert each integer to binary and count the number of ones
    arr = sorted((bin(i).count('1'), i) for i in arr)
    return [i[1] for i in arr]