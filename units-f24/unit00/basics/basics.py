x: str = "x"
y: str = "y"
z: str = x 

x = y
y = x 

print("The value of z is: " + z)

z = x + y 
z += z 

print("The value of z is: " + z)
