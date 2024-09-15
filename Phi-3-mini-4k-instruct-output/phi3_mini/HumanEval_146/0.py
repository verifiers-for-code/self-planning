def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    

 1. Create a function to check if the first and last digits of a number are odd.
2. Loop the input list, if the number is greater than 10 and both the first and last digits are odd, increment the counter.
3. Return the counter."""

    def is_odd(n):
        return n % 2 == 1

    count = 0
    for num in nums:
        if num > 10:
            first_digit = abs(num) // 10
            last_digit = abs(num) % 10
            if is_odd(first_digit) and is_odd(last_digit):
                count += 1
    return count