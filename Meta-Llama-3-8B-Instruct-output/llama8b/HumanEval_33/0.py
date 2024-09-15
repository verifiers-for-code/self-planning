def sort_third(l: list):
    non_divisible = [i for i in range(len(l)) if i % 3 != 0]
    divisible = sorted([x for i, x in enumerate(l) if i % 3 == 0])
    return [x if i not in non_divisible else divisible.pop(0) for i, x in enumerate(l)]