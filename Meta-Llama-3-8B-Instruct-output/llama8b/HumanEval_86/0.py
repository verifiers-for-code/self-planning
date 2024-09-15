def anti_shuffle(s):
    words = s.split()
    sorted_words = [''.join(sorted(word)) for word in words]
    return ' '.join(sorted_words)

print(anti_shuffle('Hi'))  # returns 'Hi'
print(anti_shuffle('hello'))  # returns 'ehllo'
print(anti_shuffle('Hello World!!!'))  # returns 'Hello !!!Wdlor'