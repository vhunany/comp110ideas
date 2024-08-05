"""
Write a program that shifts each element of a list to the right by one position. The last element should wrap around to the first position.

Example Input:
numbers = [1, 2, 3, 4, 5]

Example Output:
Shifted list: [5, 1, 2, 3, 4]
"""

numbers = [1, 2, 3, 4, 5]
index = len(numbers) - 1
last_element = numbers[-1]

while index > 0:
    numbers[index] = numbers[index - 1]
    index -= 1

numbers[0] = last_element

print("Shifted list:", numbers)