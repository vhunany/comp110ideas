x: str = "x"
y: str = "y"
z: str = x 

x = y
y = x

def test_scope(x: str, y: str, z: str) -> str: 
    z = x + y 
    z += z 

    return z

print("The value of z is: " + z)

f: str = test_scope(y, z, x)

print(f)