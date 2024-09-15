def by_length(arr):
    # Filter the array to include only numbers between 1 and 9
    filtered_arr = [num for num in arr if 1 <= num <= 9]
    
    # Sort the filtered array
    filtered_arr.sort()
    
    # Reverse the sorted array
    filtered_arr = filtered_arr[::-1]
    
    # Replace each number with its corresponding name from "One" to "Nine"
    num_names = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    result = [num_names[num] for num in filtered_arr]
    
    return result