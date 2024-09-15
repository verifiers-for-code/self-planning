def check_dict_case(dict):
    if not dict:
        return False
    
    all_keys_str = all(isinstance(key, str) for key in dict.keys())
    if not all_keys_str:
        return False
    
    all_keys_lower = all(key.islower() for key in dict.keys())
    all_keys_upper = all(key.isupper() for key in dict.keys())
    
    return all_keys_lower or all_keys_upper