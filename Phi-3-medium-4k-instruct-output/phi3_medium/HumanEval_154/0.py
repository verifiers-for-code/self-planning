def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    """
    def generate_rotations(word):
        """Generate all rotations of a word"""
        rotations = []
        for i in range(len(word)):
            rotations.append(word[i:] + word[:i])
        return rotations

    rotations = generate_rotations(b)
    for rotation in rotations:
        if rotation in a:
            return True
    return False