"""
Write a program that finds the longest contiguous subarray of positive numbers in a list.

Example Input:
numbers = [1, -2, 3, 4, -1, 2, 3, 4, 5, -6]

Example Output:
Longest subarray of positive numbers: [2, 3, 4, 5]
"""

numbers = [1, -2, 3, 4, -1, 2, 3, 4, 5, -6]
index = 0
max_length = 0
current_length = 0
max_start = 0
current_start = 0

while index < len(numbers):
    if numbers[index] > 0:
        current_length += 1
        if current_length > max_length:
            max_length = current_length
            max_start = current_start
    else:
        current_length = 0
        current_start = index + 1
    index += 1

longest_subarray = numbers[max_start:max_start + max_length]
print("Longest subarray of positive numbers:", longest_subarray)