def split_words(txt):
    words = txt.split()
    if not words:
        return [i for i, c in enumerate('abcdefghijklmnopqrstuvwxyz') if c in txt.lower() and i % 2 != 0]
    return words