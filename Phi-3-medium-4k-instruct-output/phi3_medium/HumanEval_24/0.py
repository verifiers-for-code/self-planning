def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Create a list of all numbers from 1 to n-1
    divisors = list(range(1, n))

    # Check if each number in the list divides n evenly
    even_divisors = [divisor for divisor in divisors if n % divisor == 0]

    # Return the largest number that divides n evenly
    return max(even_divisors)