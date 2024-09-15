def triangle_area(a, b, c):
    # Check if the three sides form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        # Calculate the semi-perimeter
        s = (a + b + c) / 2
        # Calculate the area using Heron's formula
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return round(area, 2)
    else:
        return -1