def fruit_distribution(s, n):
    s = s.replace(" apples", "").replace(" oranges", "").replace(" and", "").replace(" ", "")
    apples = int(s.split(" ")[0])
    oranges = int(s.split(" ")[1])
    return n - apples - oranges