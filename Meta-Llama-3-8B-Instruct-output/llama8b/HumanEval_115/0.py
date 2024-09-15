def max_fill(grid, capacity):
    total_water = sum(sum(row) for row in grid)
    total_bucket_capacity = capacity
    return math.ceil(total_water / total_bucket_capacity)