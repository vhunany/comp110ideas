def remove_all_occurrences(lst, value):
    i = 0
    while i < len(lst):
        if type(lst[i]) == list:
            # Recursively process nested lists
            remove_all_occurrences(lst[i], value)
            # Remove empty nested lists if desired
            if len(lst[i]) == 0:
                lst.pop(i)
            else:
                i += 1
        elif lst[i] == value:
            # Remove the element if it matches the specified value
            lst.pop(i)
        else:
            i += 1

# Example usage
lst1 = [1, 2, 3, 2, 4, 2, 5]
remove_all_occurrences(lst1, 2)
print(lst1)  # Output: [1, 3, 4, 5]

lst2 = [2, [1, 2, [2, 3]], 4, 2]
remove_all_occurrences(lst2, 2)
print(lst2)  # Output: [[], [1, [], [3]], 4, []]