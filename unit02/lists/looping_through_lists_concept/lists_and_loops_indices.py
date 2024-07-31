"""
Modify your solutions for the above by also printing out the index values. 
You should not instantiate new variables in order to do this or use any 
built-in functions that we have not learned, only add a print statement and use the existing variables. 
"""


# TODO: While loops
# List x
x = [9, -1, 8, 5]
i = 0
while i < len(x):
    print(f"Index {i}: {x[i]}")
    i += 1

# List y
y = ["cat", "dog", "turtle", "elephant"]
i = 0
while i < len(y):
    print(f"Index {i}: {y[i]}")
    i += 1

# List z
z = ["z"]
i = 0
while i < len(z):
    print(f"Index {i}: {z[i]}")
    i += 1


# OR...

# List x
x = [9, -1, 8, 5]
i = 0
while i < len(x):
    print(i)
    print(x[i])
    i += 1

# List y
y = ["cat", "dog", "turtle", "elephant"]
i = 0
while i < len(y):
    print(i)
    print(y[i])
    i += 1

# List z
z = ["z"]
i = 0
while i < len(z):
    print(i)
    print(x[i])
    i += 1


# TODO: for... in... range() loops
# List x
x = [9, -1, 8, 5]
for i in range(len(x)):
    print(f"Index {i}: {x[i]}")

# List y
y = ["cat", "dog", "turtle", "elephant"]
for i in range(len(y)):
    print(f"Index {i}: {y[i]}")

# List z
z = ["z"]
for i in range(len(z)):
    print(f"Index {i}: {z[i]}")

# OR...

x = [9, -1, 8, 5]
for i in range(len(x)):
    print(i)
    print(x[i])

# List y
y = ["cat", "dog", "turtle", "elephant"]
for i in range(len(y)):
    print(i)
    print(y[i])

# List z
z = ["z"]
for i in range(len(z)):
    print(i)
    print(z[i])
