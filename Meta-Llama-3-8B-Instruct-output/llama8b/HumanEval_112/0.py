def reverse_delete(s, c):
    new_string = ''.join([char for char in s if char not in c])
    return (new_string, new_string == new_string[::-1])