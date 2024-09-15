def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    
    """
    # 1. Initialize a variable to store the sum.
    sum_of_upper_chars = 0

    # 2. Loop through the string.
    for char in s:
        # 3. If the character is uppercase, add its ASCII value to the sum.
        if char.isupper():
            sum_of_upper_chars += ord(char)

    # 4. Return the sum.
    return sum_of_upper_chars