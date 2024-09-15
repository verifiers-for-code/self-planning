def minPath(grid, k):
    n = len(grid)
    freq = {}
    for i in range(n):
        for j in range(n):
            if grid[i][j] not in freq:
                freq[grid[i][j]] = 0
            freq[grid[i][j]] += 1

    result = []
    current_num = grid[0][0]
    current_path = [current_num]
    for _ in range(k):
        freq[current_num] -= 1
        if freq[current_num] == 0:
            del freq[current_num]
        result.append(current_num)
        current_path.append(current_num)
        if len(freq) == 0:
            break
        current_num = min((num for num in freq if freq[num] > 0))
    return current_path