"""
Write a program that calculates the sum of all positive numbers in a list.

Example Input:
numbers = [-3, 4, -1, 6, -2, 7]

Example Output:
Sum of positive numbers: 17
"""

numbers = [-3, 4, -1, 6, -2, 7]
index = 0
sum_positive = 0

while index < len(numbers):
    if numbers[index] > 0:
        sum_positive += numbers[index]
    index += 1

print("Sum of positive numbers:", sum_positive)