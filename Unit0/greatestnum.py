num1: float = float(input("Enter the first number: "))
num2: float = float(input("Enter the second number: "))
num3: float = float(input("Enter the third number: "))
greatest: float = num1 # challenging here becuase they have to realize that they can't let the greatest = 0.0 since all the nums 
# can be negative
# they must realize that they have to assign the greatest num to one of the 3 input values. 
# they must realize that they can do this since the greatest will be reassigned

# Compare the numbers to find the greatest
if num2 > greatest:
    greatest = num2

if num3 > greatest:
    greatest = num3

# Output the greatest number
print("The greatest number is...")
print(greatest)