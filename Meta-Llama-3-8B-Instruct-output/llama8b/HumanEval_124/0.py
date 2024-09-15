def valid_date(date):
    """
    This function validates a given date string and returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    Parameters:
    date (str): The date string to be validated.

    Returns:
    bool: True if the date is valid, False otherwise.
    """
    # Split the date string into month, day, and year
    date_parts = date.split('-')
    
    # Check if the date string is not empty
    if len(date_parts) != 3:
        return False
    
    # Check if the month is between 1 and 12
    month, day, year = map(int, date_parts)
    if month < 1 or month > 12:
        return False
    
    # Check if the day is valid for the given month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if day < 1 or day > 29:
            return False
    
    # Check if the year is valid
    if len(str(year)) != 4:
        return False
    
    return True