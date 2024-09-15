def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only's ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    

 1. Initialize a variable to store the sum.
2. Loop through the string.
3. Check if the character is uppercase.
4. If it is, add its ASCII code to the sum.
5. Return the sum."""
    sum = 0
    for char in s:
        if char.isupper():
            sum += ord(char)
    return sum