"""
Iterate through the lists and print out every element using a while loop. 
Iterate through the lists and print out every element using a for loop. 
Iterate through the lists and print out every element using a for.. in range() loop.
"""

# TODO: While loops
# List x
x = [9, -1, 8, 5]
i = 0
while i < len(x):
    print(x[i])
    i += 1

# List y
y = ["cat", "dog", "turtle", "elephant"]
i = 0
while i < len(y):
    print(y[i])
    i += 1

# List z
z = ["z"]
i = 0
while i < len(z):
    print(z[i])
    i += 1



# TODO: for loops
# List x
x = [9, -1, 8, 5]
for element in x:
    print(element)

# List y
y = ["cat", "dog", "turtle", "elephant"]
for element in y:
    print(element)

# List z
z = ["z"]
for element in z:
    print(element)



# TODO: for... in... range() loops
# List x
x = [9, -1, 8, 5]
for i in range(len(x)):
    print(x[i])

# List y
y = ["cat", "dog", "turtle", "elephant"]
for i in range(len(y)):
    print(y[i])

# List z
z = ["z"]
for i in range(len(z)):
    print(z[i])

