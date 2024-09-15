def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """

    # 1. Create a function to count unique characters in a string.
    def count_unique_chars(word):
        return len(set(word))

    # 2. Create a list of tuples, each containing a word and its unique character count.
    word_counts = [(word, count_unique_chars(word)) for word in words]

    # 3. Sort the list of tuples by the unique character count in descending order, and then by the word in ascending order.
    word_counts.sort(key=lambda x: (-x[1], x[0]))

    # 4. Return the first element of the sorted list.
    return word_counts[0][0]