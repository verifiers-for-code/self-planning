def odd_count(lst):
    result = []
    for i, s in enumerate(lst):
        odd_count = sum(1 for c in s if int(c) % 2 != 0)
        result.append(f"the number of odd elements {odd_count}n the str{odd_count}ng {i+1} of the {i+1}nput.")
    return result