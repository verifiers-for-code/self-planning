def solve(N):
    # Convert the integer to binary and remove the '0b' prefix
    binary = bin(N)[2:]
    
    # Initialize a variable to store the sum of the digits
    total_sum = 0
    
    # Loop through each character in the binary string
    for digit in binary:
        # Add the integer value of the character to the sum
        total_sum += int(digit)
    
    # Return the sum as a string
    return str(total_sum)