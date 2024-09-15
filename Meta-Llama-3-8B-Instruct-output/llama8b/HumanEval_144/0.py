def simplify(x, n):
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    product_num = x_num * n_num
    product_den = x_den * n_den
    gcd = lambda a, b: a if not b else gcd(b, a % b)
    common_divisor = gcd(product_num, product_den)
    product_num //= common_divisor
    product_den //= common_divisor
    return product_num == product_den