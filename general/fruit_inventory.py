# Function Definitions

def add_fruit(fruit_inventory, fruit_name, quantity):
    if fruit_name in fruit_inventory:
        fruit_inventory[fruit_name] += quantity
    else:
        fruit_inventory[fruit_name] = quantity
    print(f"Added {quantity} {fruit_name}(s).")

def remove_fruit(fruit_inventory, fruit_name, quantity):
    if fruit_name in fruit_inventory:
        if fruit_inventory[fruit_name] >= quantity:
            fruit_inventory[fruit_name] -= quantity
            print(f"Removed {quantity} {fruit_name}(s).")
        else:
            print(f"Not enough {fruit_name} to remove.")
    else:
        print(f"{fruit_name} not found in inventory.")

def list_fruits(fruit_inventory):
    if fruit_inventory:
        print("Current fruit inventory:")
        for fruit in fruit_inventory:
            print(f"- {fruit}: {fruit_inventory[fruit]}")
    else:
        print("No fruits in inventory.")

# Main Program

fruit_inventory = {}

running = True

while running:
    print("\nFruit Inventory Menu:")
    print("1. Add fruit")
    print("2. Remove fruit")
    print("3. List all fruits")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        fruit_name = input("Enter fruit name: ")
        quantity = int(input("Enter quantity: "))
        add_fruit(fruit_inventory, fruit_name, quantity)
    elif choice == '2':
        fruit_name = input("Enter fruit name: ")
        quantity = int(input("Enter quantity to remove: "))
        remove_fruit(fruit_inventory, fruit_name, quantity)
    elif choice == '3':
        list_fruits(fruit_inventory)
    elif choice == '4':
        print("Exiting the program.")
        running = False
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
