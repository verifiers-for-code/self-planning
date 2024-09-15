from itertools import product

def minPath(grid, k):
    n = len(grid)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    min_path = []
    min_lex_val = float('inf')

    def get_neighbors(x, y):
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                neighbors.append((nx, ny))
        return neighbors

    def dfs(x, y, path, visited):
        nonlocal min_path, min_lex_val
        if len(path) == k:
            lex_val = int(''.join(map(str, path)))
            if lex_val < min_lex_val:
                min_lex_val = lex_val
                min_path = path
            return
        for nx, ny in get_neighbors(x, y):
            if (nx, ny) not in visited:
                dfs(nx, ny, path + [grid[nx][ny]], visited | {(nx, ny)})

    for i in range(n):
        for j in range(n):
            dfs(i, j, [grid[i][j]], {(i, j)})

    return min_path