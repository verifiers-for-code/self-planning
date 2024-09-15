def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            ascii_offset = 97 if char.islower() else 65
            result += chr((ord(char) - ascii_offset + 2 * 2) % 26 + ascii_offset)
        else:
            result += char
    return result

print(encrypt('hi'))  # returns 'lm'
print(encrypt('asdfghjkl'))  # returns 'ewhjklnop'
print(encrypt('gf'))  # returns 'kj'
print(encrypt('et'))  # returns 'ix'