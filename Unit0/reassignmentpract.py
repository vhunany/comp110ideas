x: str = "y"
y: str = "x"
z: str = x # "y"
w: str = z # "y"

if not not w != "z":
    if y == x:
        print("Mellon")
    elif not z == "x" and w != y:
        print("Carrot")
        if "x" != "y": 
            print(str("juice"))
    elif x == "y" or z == "w":
        print("Spinach")
else:
    print("Juice")

print("!")
print(":" + str("P"))  # Concatenating then printing the concatenated string and understanding the diff between printing them individually