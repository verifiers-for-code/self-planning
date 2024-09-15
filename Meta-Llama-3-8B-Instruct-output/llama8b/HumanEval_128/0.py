def prod_signs(arr):
    if not arr:
        return None
    sign_product = 1
    sum_magnitudes = 0
    for num in arr:
        if num == 0:
            sign_product = 0
        elif num > 0:
            sum_magnitudes += num
        else:
            sign_product *= -1
            sum_magnitudes += num
    return sign_product * sum_magnitudes