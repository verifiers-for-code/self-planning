from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary to map the words to their corresponding integer values.
    word_to_int = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    # Split the input string into a list of words.
    words = numbers.split()

    # Sort the list of words based on their corresponding integer values.
    sorted_words = sorted(words, key=lambda word: word_to_int[word])

    # Join the sorted list of words into a string and return it.
    return ' '.join(sorted_words)