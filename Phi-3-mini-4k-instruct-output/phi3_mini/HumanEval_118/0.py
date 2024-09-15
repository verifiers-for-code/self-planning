def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    

    1. Create a list of vowels.
    2. Create a list of consonants.
    3. Loop the word from the right side.
    4. If the current character is a vowel, return it.
    5. If the current character is a consonant, return the previous vowel.
    6. If no vowel is found, return an empty string."""
    
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    consonants = [chr(i) for i in range(ord('a'), ord('z')+1) if chr(i) not in vowels]
    
    for i in range(len(word)-1, -1, -1):
        if word[i] in vowels:
            return word[i]
        elif word[i] in consonants:
            for j in range(i-1, -1, -1):
                if word[j] in vowels:
                    return word[j]
    return ""