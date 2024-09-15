def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    # Split the string into words
    words = s.split()
    
    # Create a list to store the words that meet the criteria
    result = []
    
    # Loop through the words, count the consonants in each word
    for word in words:
        consonants = sum(1 for c in word if c.lower() in 'bcdfghjklmnpqrstvwxyz')
        
        # If the count of consonants is equal to n, add the word to the list
        if consonants == n:
            result.append(word)
    
    # Return the list
    return result