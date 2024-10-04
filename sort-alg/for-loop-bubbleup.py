def bubble_up_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                # Swap elements without tuple unpacking
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp

def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_index = i  # Assume the minimum is the first element in the unsorted part
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j  # Update the index of the minimum element
        # Swap the found minimum element with the first element
        if min_index != i:
            temp = lst[i]
            lst[i] = lst[min_index]
            lst[min_index] = temp

def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        key = lst[i]  # The element to be positioned
        j = i - 1
        # Move elements of lst[0..i-1] that are greater than key to one position ahead
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key  # Place the key in its correct position

# List to be sorted
my_list = [64, 34, 25, 12, 22, 11, 90]
print("Our list that needs sorting:", my_list)


# Bubble Sort
bubble_sorted_lst = my_list.copy()  # Copy the list for sorting
bubble_up_sort(bubble_sorted_lst)
print("Bubble Sort Result:", bubble_sorted_lst)

# Selection Sort
selection_sorted_lst = my_list.copy()  # Copy the list for sorting
selection_sort(selection_sorted_lst)
print("Selection Sort Result:", selection_sorted_lst)

# Insertion Sort
insertion_sorted_lst = my_list.copy()  # Copy the list for sorting
insertion_sort(insertion_sorted_lst)
print("Insertion Sort Result:", insertion_sorted_lst)

