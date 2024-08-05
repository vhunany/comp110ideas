def increment_values(dct):
    for key in dct:
        value = dct[key]
        if type(value) == int:
            # Increment the integer value by 1
            dct[key] = value + 1
        elif type(value) == dict:
            # Recursively call the function for nested dictionary
            increment_values(value)
        # If the value is neither int nor dict, do nothing
        # (The function doesn't alter non-integer, non-dictionary values)

# Example usage
dct1 = {'a': 1, 'b': 2, 'c': 3}
increment_values(dct1)
print(dct1)  # Output: {'a': 2, 'b': 3, 'c': 4}

dct2 = {'x': 5, 'y': {'a': 1, 'b': 2}, 'z': 3}
increment_values(dct2)
print(dct2)  # Output: {'x': 6, 'y': {'a': 2, 'b': 3}, 'z': 4}

dct3 = {'key1': 7, 'key2': 'string', 'key3': {'inner_key': 10, 'another_key': [1, 2, 3]}}
increment_values(dct3)
print(dct3)  # Output: {'key1': 8, 'key2': 'string', 'key3': {'inner_key': 11, 'another_key': [1, 2, 3]}}
