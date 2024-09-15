def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    

 1. Check if the dictionary is empty.
2. If the dictionary is not empty, check if all keys are strings.
3. If all keys are strings, check if they are all in lower case or all in upper case.
4. Return True if all keys are in the same case, else return False."""

    # Check if the dictionary is empty
    if not dict:
        return False

    # Check if all keys are strings
    if not all(isinstance(key, str) for key in dict.keys()):
        return False

    # Check if all keys are in the same case
    first_key_case = None
    for key in dict.keys():
        if first_key_case is None:
            first_key_case = key.islower()
        elif (key.islower() and not first_key_case) or (key.isupper() and first_key_case):
            return False

    return True