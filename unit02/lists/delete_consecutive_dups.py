"""
Write a program that finds all consecutive duplicates in a list and replaces them with a single occurrence.

Example Input:
characters = ['a', 'a', 'b', 'c', 'c', 'c', 'd']

Example Output:
Modified list: ['a', 'b', 'c', 'd']
"""

characters = ['a', 'a', 'b', 'c', 'c', 'c', 'd']
index = 0

while index < len(characters) - 1:
    if characters[index] == characters[index + 1]:
        characters.pop(index)
    else:
        index += 1

print("Modified list:", characters)