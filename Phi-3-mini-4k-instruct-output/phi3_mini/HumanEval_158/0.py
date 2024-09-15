def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    

 1. Create a function to find the word with maximum unique characters.
2. Loop the list of words.
3. For each word, count the number of unique characters.
4. If the number of unique characters is greater than the current maximum, update the maximum and the result.
5. If the number of unique characters is equal to the current maximum, compare the words lexicographically and update the result if necessary.
6. Return the result."""
    max_word = ""
    max_unique_chars = 0
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars or (unique_chars == max_unique_chars and word < max_word):
            max_word = word
            max_unique_chars = unique_chars
    return max_word