def car_race_collision(n: int):
    collisions = 0
    left_cars = []
    right_cars = []
    
    for i in range(n):
        left_cars.append(i)
        right_cars.append(n - i - 1)
    
    for i in range(n):
        if left_cars[i] == right_cars[n - i - 1]:
            collisions += 1
            left_cars.pop(i)
            right_cars.pop(n - i - 1 - 1)
            i -= 1
    
    return collisions