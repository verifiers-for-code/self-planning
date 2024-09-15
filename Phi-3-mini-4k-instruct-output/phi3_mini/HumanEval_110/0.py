def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    
    """
    def is_even(num):
        """Check if a number is even."""
        return num % 2 == 0
    
    # Loop through lst1 and check if each element is even
    for num in lst1:
        if not is_even(num):
            # If any element is odd, loop through lst2 and check if there is an even number
            for even_num in lst2:
                if is_even(even_num):
                    # Exchange the odd element in lst1 with the even element in lst2
                    lst1[lst1.index(num)] = even_num
                    lst2[lst2.index(even_num)] = num
                    break
            else:
                # If there is no even number in lst2, return "NO"
                return "NO"
    
    # If all elements in lst1 are even, return "YES"
    return "YES"