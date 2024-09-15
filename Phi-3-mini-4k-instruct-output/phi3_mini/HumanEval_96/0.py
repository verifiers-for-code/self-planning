def count_up_to(n):
    """Implement a function that takes a non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    

 1. Create a function to check if a number is prime.
2. Create an empty list to store the prime numbers.
3. Loop from 2 to n, check if the number is prime, if yes, append it to the list.
4. Return the list."""

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes