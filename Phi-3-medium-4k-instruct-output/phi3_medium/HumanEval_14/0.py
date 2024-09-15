from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # 1. Create an empty list to store the prefixes.
    prefixes = []

    # 2. Loop through the string, and for each character, add the substring from the start to the current character to the list of prefixes.
    for i in range(len(string)):
        prefixes.append(string[:i+1])

    # 3. Return the list of prefixes.
    return prefixes