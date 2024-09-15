from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    # 1. Create an empty list for integers.
    integers = []

    # 2. Loop through the given list.
    for value in values:
        # 3. Check if the current value is an integer, if yes, append it to the integer list.
        if isinstance(value, int):
            integers.append(value)

    # 4. Return the integer list.
    return integers