def get_closest_vowel(word):
    result = ""
    is_vowel_found = False
    for char in reversed(word):
        if char.lower() in 'aeiou':
            if not is_vowel_found:
                is_vowel_found = True
                result = char
        elif is_vowel_found:
            break
    return result