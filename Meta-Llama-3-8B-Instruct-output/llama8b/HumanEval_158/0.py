def find_max(words):
    max_count = 0
    max_word = ""
    word_count = {}
    
    for word in words:
        unique_chars = set(word)
        word_count[word] = len(unique_chars)
        
        if word_count[word] > max_count:
            max_count = word_count[word]
            max_word = word
        elif word_count[word] == max_count:
            max_word = min(max_word, word)
    
    return max_word