def tri(n):
    tribonacci_sequence = [1, 3, 2]
    for i in range(3, n + 1):
        if i % 2 == 0:
            tribonacci_sequence.append(1 + i / 2)
        else:
            tribonacci_sequence.append(tribonacci_sequence[i - 1] + tribonacci_sequence[i - 2] + tribonacci_sequence[i - 3])
    return tribonacci_sequence