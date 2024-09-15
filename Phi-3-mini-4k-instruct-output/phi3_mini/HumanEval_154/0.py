def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    

 1. Create a function to check if a word is a rotation of another word.
2. Check if the second word or any of its rotations is a substring in the first word.
3. Return True if found, otherwise return False."""

    def is_rotation(word1, word2):
        if len(word1) != len(word2):
            return False
        return word1 in (word2 + word2)

    for i in range(len(b)):
        if is_rotation(b, b[i:] + b[:i]):
            if b[i:] in a:
                return True
    return False