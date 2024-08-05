def add_item(inventory, item, quantity):
    item_found = False
    for key in inventory:
        if key == item:
            item_found = True
            inventory[key] += quantity
    if not item_found:
        inventory[item] = quantity

def remove_item(inventory, item, quantity):
    for key in inventory:
        if key == item:
            inventory[key] -= quantity
            if inventory[key] < 0:
                inventory[key] = 0
            return  # Exit the function after updating the item

def total_items(inventory):
    count = 0
    for item in inventory:
        count += 1
    return count

def low_stock_items(inventory, threshold):
    low_stock = []
    for item in inventory:
        if inventory[item] < threshold:
            low_stock.append(item)
    return low_stock

def main():
    inventory = {
        'Apples': 30,
        'Oranges': 15,
        'Bananas': 20
    }

    # Add items
    add_item(inventory, 'Apples', 10)
    add_item(inventory, 'Pears', 5)

    # Remove items
    remove_item(inventory, 'Oranges', 10)
    remove_item(inventory, 'Bananas', 25)

    # Total number of items
    print("Total number of items:", total_items(inventory))  # 3

    # Items below threshold
    print("Items below threshold of 15:", low_stock_items(inventory, 15))  # ['Pears', 'Oranges']

# Run the main function
if __name__ == "__main__":
    main()