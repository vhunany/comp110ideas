def add_item(inventory, item, quantity) -> None:
    item_found = False
    for key in inventory:
        if key == item:
            inventory[key] += quantity
            item_found = True

    if not item_found:
        inventory[item] = quantity

def remove_item(inventory, item, quantity) -> None:
    item_found = False
    for key in inventory:
        if key == item:
            inventory[key] -= quantity
            if inventory[key] < 0:
                inventory[key] = 0
            item_found = True

def main():
    inventory = {
        'Apples': 30,
        'Oranges': 15,
        'Bananas': 20
    }

    add_item(inventory, 'Apples', 10)
    remove_item(inventory, 'Bananas', 25)

    print("Current inventory:", inventory)

if __name__ == "__main__":
    main()
