def fix_spaces(text):
    result = ""
    prev_char = ""
    for char in text:
        if char == " ":
            if prev_char == " ":
                result += "-"
            else:
                result += "_"
        else:
            result += char
        prev_char = char
    return result