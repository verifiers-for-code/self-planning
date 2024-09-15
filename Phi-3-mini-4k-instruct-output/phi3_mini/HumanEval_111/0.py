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

    

 1. Split the string into a list of letters.
2. Create a dictionary to store the frequency of each letter.
3. Loop the list of letters, increment the frequency of each letter in the dictionary.
4. Find the maximum frequency.
5. Create a list of letters with the maximum frequency.
6. Return the dictionary of letters with the maximum frequency."""

    # Step 1: Split the string into a list of letters
    letters = test.split()

    # Step 2: Create a dictionary to store the frequency of each letter
    freq_dict = {}

    # Step 3: Loop the list of letters, increment the frequency of each letter in the dictionary
    for letter in letters:
        if letter in freq_dict:
            freq_dict[letter] += 1
        else:
            freq_dict[letter] = 1

    # Step 4: Find the maximum frequency
    max_freq = max(freq_dict.values())

    # Step 5: Create a list of letters with the maximum frequency
    max_freq_letters = [letter for letter, freq in freq_dict.items() if freq == max_freq]

    # Step 6: Return the dictionary of letters with the maximum frequency
    return {letter: max_freq for letter in max_freq_letters}