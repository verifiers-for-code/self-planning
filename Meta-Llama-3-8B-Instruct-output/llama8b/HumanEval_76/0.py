def is_simple_power(x, n):
    import math
    if n <= 0:
        return False
    root = round(math.pow(n, 1.0 / math.log(x, n)))
    return root == int(root) and root > 0