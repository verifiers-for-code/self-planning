def closest_integer(value):
    value = float(value)
    if value - int(value) < 0.5:
        return int(value)
    else:
        return int(round(value))