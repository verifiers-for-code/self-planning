def sort_array(array):
    if not array:
        return array

    first_last_sum = array[0] + array[-1]
    if first_last_sum % 2 == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array)