"""Simplified Crumbl Cookies Shop - Functions Version!"""

def add_cookie(menu, name, price):
    menu.append({"name": name, "price": price})

def display_menu(menu):
    print("Menu:")
    i = 0
    for cookie in menu:
        i += 1
        print(f"{i}. {cookie['name']} - ${cookie['price']:.2f}")

def take_order(menu):
    order = {}
    name = input("Enter your name: ")
    date = input("Enter the date (mm-dd-yyyy): ")

    display_menu(menu)

    choice = 1
    while choice != 0:
        choice = int(input(f"Choose a cookie number (1-{len(menu)}) or 0 to finish: "))
        if 1 <= choice <= len(menu):
            cookie = menu[choice - 1]
            amount = int(input(f"How many {cookie['name']} cookies do you want? "))
            if cookie['name'] in order:
                order[cookie['name']] += amount
            else:
                order[cookie['name']] = amount

    if input("Would you like to remove any items from your order? (yes/no): ").lower() == 'yes':
        remove_item(order)

    show_receipt(order, menu, name, date)

def remove_item(order):
    bool_condition: bool = True
    while bool_condition:
        print("\nCurrent Order:")
        for cookie_name in order:
            print(f"{cookie_name}: {order[cookie_name]}")

        item_to_remove = input("Enter the name of the cookie you want to remove or enter 'none' to exist: ")


        if item_to_remove in order:
            remove_amount = int(input(f"How many {item_to_remove} cookies would you like to remove? "))
            if remove_amount >= order[item_to_remove]:
                order.pop(item_to_remove)
            else:
                order[item_to_remove] -= remove_amount
        else:
            if item_to_remove == "none": 
                bool_condition = False
            else: 
                print(f"No such cookie '{item_to_remove}' in your order.")


def show_receipt(order, menu, name, date):
    print("\n---- Receipt: ----")
    print(f"Name: {name}")
    print(f"Date: {date}")
    total = 0
    for cookie_name in order:
        for cookie in menu:
            if cookie['name'] == cookie_name:
                cost = cookie['price'] * order[cookie_name]
                total += cost
                print(f"{order[cookie_name]} x {cookie_name}: ${cost:.2f}")
    print(f"Total: ${total:.2f}")
    print("__________________")

def main():
    menu = []
    add_cookie(menu, "Chocolate Chip", 2.50)
    add_cookie(menu, "Oatmeal Raisin", 2.00)
    add_cookie(menu, "Strawberry Cake", 3.50)
    add_cookie(menu, "Cinnamon Crunch", 2.95)
    
    take_order(menu)

if __name__ == "__main__":
    main()
