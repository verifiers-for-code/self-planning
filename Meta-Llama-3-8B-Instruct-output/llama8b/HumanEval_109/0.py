def move_one_ball(arr):
    if not arr:
        return True

    max_element = max(arr)
    shift_count = 0

    for i in range(len(arr)):
        if arr[i] < max_element:
            shift_count += 1
        else:
            max_element = arr[i]

    return shift_count == 0