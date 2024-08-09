def remove_values_from_dict(input_dict, values_to_remove):
    # Convert list of values to remove into a list (not using set)
    values_list = values_to_remove
    removed_count = 0

    # Collect keys to remove
    keys_to_remove = []
    for key in input_dict:
        if input_dict[key] in values_list:
            keys_to_remove.append(key)

    # Remove keys from the dictionary
    for key in keys_to_remove:
        if input_dict[key] in values_list:
            input_dict.pop(key)  # Remove the key-value pair from the dictionary
            removed_count += 1  # Increment the removed count

    return removed_count

# Test cases
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
values_list = [2, 4]
print(remove_values_from_dict(my_dict, values_list))  
# Output: 2 (since the values 2 and 4 are removed)

# After removal, the dictionary should be {'a': 1, 'c': 3}
print(my_dict)  
# Output: {'a': 1, 'c': 3}

another_dict = {'x': 'apple', 'y': 'banana', 'z': 'cherry'}
values_to_remove = ['banana', 'cherry']
print(remove_values_from_dict(another_dict, values_to_remove))  
# Output: 2 (since the values 'banana' and 'cherry' are removed)

# After removal, the dictionary should be {'x': 'apple'}
print(another_dict)  
# Output: {'x': 'apple'}
