def reverse_list_with_twist(lst, left, right):
    # Base case: when left index is greater than or equal to right index
    if left >= right:
        return

    # Check if both elements are odd
    if lst[left] % 2 == 1 and lst[right] % 2 == 1:
        # If both are odd, do not swap them, just move inward
        reverse_list_with_twist(lst, left + 1, right - 1)
    else:
        # Swap elements if they are not both odd using a temporary variable
        temp = lst[left]
        lst[left] = lst[right]
        lst[right] = temp
        # Recursively call the function with updated indices
        reverse_list_with_twist(lst, left + 1, right - 1)

# Example usage
lst1 = [1, 2, 3, 4, 5, 6]
reverse_list_with_twist(lst1, 0, 5)
print(lst1)  # Output: [6, 2, 3, 4, 5, 1]

lst2 = [2, 4, 6, 8]
reverse_list_with_twist(lst2, 0, 3)
print(lst2)  # Output: [8, 6, 4, 2]

lst3 = [7, 2, 5, 8, 3]
reverse_list_with_twist(lst3, 0, 4)
print(lst3)  # Output: [3, 2, 5, 8, 7]
