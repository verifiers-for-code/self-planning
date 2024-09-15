def exchange(lst1, lst2):
    even_lst1 = set([num for num in lst1 if num % 2 == 0])
    even_lst2 = set([num for num in lst2 if num % 2 == 0])
    if even_lst1.issubset(even_lst2):
        return "YES"
    else:
        return "NO"