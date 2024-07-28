"""
Vegetable Basket Price Calculator
This program calculates the total price of a basket of vegetables picked from a farm. 
"""

# TODO: Write Up
"""
Must comment your code. Comments must be explain in your own words what you are doing in each line. 
Ex. 
star: str = "Pretty"  # instantiating that variable star and assigning it to a str value 

Due by the end of the day, they have the full class time to do it. No late submissions. This is so, a video solution can be posted after the due date
since we would only have less than a day to get them back for students to review. Making this a CQ instead of part of the review questions will make sure, 
everyone does some bit of review especially on the most commonly missed ideas. 
"""

# TODO: # video lesson
"""
Topics include: 
- fully evaluating lines before assigning anything to a variable 
- identifying (asking yourself) what is it that you are assigning a variable
    - if this is a str, how do you know
    - if this is an int, how do you know
    - if this is another variable, how do you know it's another variable
        - what if we are assignming one variable to another, what does this actually mean? (ex. when we refer
        to variables outside of declaring that varible, we are always looking at the value that the variable holds)
"""

# Constants for vegetable prices (price per unit in dollars)
CARROT_PRICE = 0.5
POTATO_PRICE = 0.3
TOMATO_PRICE = 0.8
LETTUCE_PRICE = 1.2

# Welcome message
print("Welcome to the Vegetable Basket Price Calculator!")

# Get user input for the quantity of each vegetable
carrots = int(input("Enter the number of carrots picked: "))
potatoes = int(input("Enter the number of potatoes picked: "))
tomatoes = int(input("Enter the number of tomatoes picked: "))
lettuce = int(input("Enter the number of lettuce heads picked: "))

# Calculate the price for each type of vegetable
carrot_cost = carrots * CARROT_PRICE
potato_cost = potatoes * POTATO_PRICE
tomato_cost = tomatoes * TOMATO_PRICE
lettuce_cost = lettuce * LETTUCE_PRICE

# Calculate the total cost
total_cost = carrot_cost + potato_cost + tomato_cost + lettuce_cost

# Apply discount if the total cost exceeds a certain amount
discount = 0.0  # Initialize discount variable
if total_cost > 20:
    discount = 0.1  # 10% discount
    total_cost *= (1 - discount)  # Apply discount
    print(f"Discount applied: {discount * 100}%")
elif total_cost > 10:
    discount = 0.05  # 5% discount
    total_cost *= (1 - discount)  # Apply discount
    print(f"Discount applied: {discount * 100}%")
else:
    print("No discount applied.")

# Print the total cost
print(f"Total cost after discount: ${total_cost:.2f}")

# Check if the user qualifies for a free gift based on the quantity of vegetables
free_gift = False  # Initialize free_gift variable

# Use boolean expressions to determine if a free gift is earned
if carrots > 10 or potatoes > 10 or tomatoes > 10 or lettuce > 5:
    free_gift = True
    print("Congratulations! You've earned a free vegetable peeler!")
elif total_cost > 15:
    free_gift = True
    print("Congratulations! You've earned a free vegetable recipe book!")
else:
    free_gift = False
    print("Thank you for shopping with us!")