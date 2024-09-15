def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of 
    the fruits in the basket return the number of the mango fruits in the basket.
    for example:
    fruit_distribution("5 apples and 6 oranges", 19) -> 19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges", 3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges", 120) -> 120 - 100 - 1 = 19
    

    1. Extract the numbers of oranges and apples from given string.
    2. Calculate the sum of oranges and apples.
    3. Deduct the sum from the total number of fruits.
    4. Return the number of mangoes.
    """
    # Split the string into words
    words = s.split()
    
    # Initialize counters for apples and oranges
    apples = 0
    oranges = 0
    
    # Iterate over the words to find the counts of apples and oranges
    for word in words:
        if word.endswith('apples'):
            apples = int(word.split('apples')[0]) if word.split('apples')[0].isdigit() else 0
        elif word.endswith('oranges'):
            oranges = int(word.split('oranges')[0]) if word.split('oranges')[0].isdigit() else 0
    
    # Calculate the number of mangoes
    mangoes = n - apples - oranges
    
    # Return the number of mangoes
    return mangoes