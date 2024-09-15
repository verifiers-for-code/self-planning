def f(n):
    result = [0] * n
    for i in range(1, n+1):
        if i % 2 == 0:
            result[i-1] = 1
            for j in range(2, i+1):
                result[i-1] *= j
        else:
            result[i-1] = sum(range(1, i+1))
    return result