def solution(lst):
    sum_odd_in_even_positions = 0
    for i, num in enumerate(lst):
        if i % 2 == 0 and num % 2 != 0:
            sum_odd_in_even_positions += num
    return sum_odd_in_even_positions