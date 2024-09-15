def fibfib(n: int):
    memo = {0: 0, 1: 0, 2: 1}
    for i in range(3, n + 1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    return memo[n]