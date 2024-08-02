"""
Cookie Shop Simulation - Crumbl
"""

# To run, do not click the play button at the top right. Run the file as a module
# python -m unit03.exercises.crumblcookies

from __future__ import annotations
from datetime import datetime

class Cookie:
    name: str
    limited_time: bool
    base_price: float

    def __init__(self, name: str, limited_time: bool, base_price: float):
        self.name = name
        self.limited_time = limited_time
        self.base_price = base_price

    def price(self) -> float:
        if self.limited_time: 
            self.base_price += 1
        
        return self.base_price


class Crumbl:
    menu: list[Cookie]
    order_log: dict[str, dict[str, int]]  # keys are names of people who ordered; values are dictionaries with date as key and amount as value

    def __init__(self):
        self.menu = []
        self.order_log = {}  # Initialize order_log to track orders by person and date

    def add_cookie(self, cookie: Cookie):
        self.menu.append(cookie)

    def make_an_order(self):
        order = {}
        person_name = input("Enter your name: ").strip()  # Ask for the person's name
        order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current date and time

        print("Available cookies:")
        for i, cookie in enumerate(self.menu): # instead of i and cookie being being iterated through, use a while loop to keep track of i and a for loop for the cookie
            print(f"{i + 1}. {cookie.name} - ${cookie.price()}")

        while True:
            choice = int(input(f"Enter the number of the cookie you want to order (1 to {len(self.menu)}), or 0 to finish: ").strip())
            if choice == 0:
                break
            if 1 <= choice <= len(self.menu):
                cookie = self.menu[choice - 1]

                while True:
                    amount = int(input(f"Enter the amount for {cookie.name} (1-12): ").strip())
                    if 1 <= amount <= 12:
                        if cookie.name in order:
                            order[cookie.name] += amount
                        else:
                            order[cookie.name] = amount
                        break  # Exit inner loop and go back to main menu
                    else:
                        print("Please enter a valid amount between 1 and 12.")
            else:
                print("Invalid choice. Please select a valid cookie number.")

        # Allow user to review and remove items before finalizing
        while True:
            print("\nCurrent Order:")
            for cookie_name in order:
                print(f"{cookie_name}: {order[cookie_name]}")

            choice = input("\nWould you like to remove any items from your order? (yes/no): ").strip().lower()
            if choice == 'yes':
                remove_name = input("Enter the name of the cookie to remove: ").strip()
                if remove_name in order:
                    while True:
                        remove_amount = int(input(f"Enter the amount of {remove_name} to remove (1-{order[remove_name]}): ").strip())
                        if 1 <= remove_amount <= order[remove_name]:
                            if remove_amount == order[remove_name]:
                                order.pop(remove_name)
                            else:
                                order[remove_name] -= remove_amount
                            break  # Exit loop after successful removal
                        else:
                            print(f"Please enter a valid amount between 1 and {order[remove_name]}.")
                else:
                    print(f"No such cookie '{remove_name}' in your order.")
            elif choice == 'no':
                break
            else:
                print("Please enter 'yes' or 'no'.")

        # Log the order by person and date
        if person_name not in self.order_log:
            self.order_log[person_name] = {}
        
        if order_date not in self.order_log[person_name]:
            self.order_log[person_name][order_date] = 0
        
        for cookie_name in order:
            self.order_log[person_name][order_date] += order[cookie_name]

        self.receipt(order)

    def receipt(self, order):
        total_price = 0
        print("\nReceipt:")
        for cookie_name in order:
            cookie = next(c for c in self.menu if c.name == cookie_name)
            price = cookie.price()
            total_price += price * order[cookie_name]
            print(f"{cookie_name}: {order[cookie_name]} x ${price:.2f} = ${price * order[cookie_name]:.2f}")

        print(f"Total Price: ${total_price:.2f}")

    def __str__(self):
        return f"Crumbl with {len(self.menu)} available cookies and {len(self.order_log)} orders in the log."


def main(): 
    # Example Usage:
    crumbl_shop = Crumbl()

    print("Status of shop at Opening: ", crumbl_shop)

    # Adding new cookies to the Crumbl menu
    crumbl_shop.add_cookie(Cookie("Milk Chocolate Chip", False, 2.75))
    crumbl_shop.add_cookie(Cookie("Cookies & Cream Cheesecake", False, 3.25))
    crumbl_shop.add_cookie(Cookie("Double Fudge Sandwich", False, 3.00))
    crumbl_shop.add_cookie(Cookie("Strawberry Cake", True, 3.50))
    crumbl_shop.add_cookie(Cookie("Cinnamon Crunch", False, 2.95))

    print("Status of shop at after recieving store deliveries: ", crumbl_shop)

    crumbl_shop.make_an_order()

    print("Current Order Log: ", crumbl_shop.order_log)

    print("Current status of the shop: ", crumbl_shop)

if __name__ == "__main__":
    main()