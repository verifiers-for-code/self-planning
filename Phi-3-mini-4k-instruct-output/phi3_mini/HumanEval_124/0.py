def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    

 1. Check if the date string is empty.
2. Split the date string by '-' and check if the format is correct.
3. Split the date string by '/' and check if the format is correct.
4. Check if the month is between 1 and 12.
5. Check if the day is between 1 and 31 for months 1,3,5,7,8,10,12.
6. Check if the day is between 1 and 30 for months 4,6,9,11.
7. Check if the day is between 1 and 29 for the month 2.
8. Return True if all conditions are met, otherwise return False."""

    # Check if the date string is empty
    if not date:
        return False

    # Split the date string by '-' and check if the format is correct
    try:
        month, day, year = date.split('-')
    except ValueError:
        return False

    # Split the date string by '/' and check if the format is correct
    try:
        month, day, year = date.split('/')
    except ValueError:
        return False

    # Check if the month is between 1 and 12
    if not (1 <= int(month) <= 12):
        return False

    # Check if the day is between 1 and 31 for months 1,3,5,7,8,10,12
    if int(month) in [1, 3, 5, 7, 8, 10, 12] and not (1 <= int(day) <= 31):
        return False

    # Check if the day is between 1 and 30 for months 4,6,9,11
    if int(month) in [4, 6, 9, 11] and not (1 <= int(day) <= 30):
        return False

    # Check if the day is between 1 and 29 for the month 2
    if int(month) == 2 and not (1 <= int(day) <= 29):
        return False

    # Check if the year is a valid integer
    try:
        int(year)
    except ValueError:
        return False

    # If all conditions are met, return True
    return True