def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}
    """
    # 1. Split the string into a list of characters.
    chars = test.split()
    
    # 2. Create a dictionary to store the frequency of each character.
    freq = {}
    
    # 3. Loop through the list of characters, update the frequency in the dictionary.
    for char in chars:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    # 4. Find the maximum frequency.
    max_freq = max(freq.values())
    
    # 5. Create a list of characters that have the maximum frequency.
    max_chars = [char for char, count in freq.items() if count == max_freq]
    
    # 6. Return a dictionary with the characters and their frequency.
    return {char: max_freq for char in max_chars}