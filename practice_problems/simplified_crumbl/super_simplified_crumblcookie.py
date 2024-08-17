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
    
    print(f"{name}, you ordered the following on {date}: {order}")

def main():
    menu = []
    add_cookie(menu, "Chocolate Chip", 2.50)
    add_cookie(menu, "Oatmeal Raisin", 2.00)
    add_cookie(menu, "Strawberry Cake", 3.50)
    add_cookie(menu, "Cinnamon Crunch", 2.95)
    
    take_order(menu)

if __name__ == "__main__":
    main()
