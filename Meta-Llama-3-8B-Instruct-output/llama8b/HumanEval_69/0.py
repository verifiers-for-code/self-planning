def search(lst):
    frequency_dict = {}
    for num in lst:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    for num, freq in frequency_dict.items():
        if freq >= num and num > 0:
            return num
    return -1