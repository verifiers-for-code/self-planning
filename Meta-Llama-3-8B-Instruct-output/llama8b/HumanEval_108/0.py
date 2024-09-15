def count_nums(arr):
    count = 0
    for num in arr:
        if num < 0:
            num = str(num)[1:]
            num = -int(num)
        else:
            num = int(str(num))
        if sum(int(digit) for digit in str(num)) > 0:
            count += 1
    return count