## Simplified Crumbl Cookies Shop - Functions Version

#### This program simulates a cookie shop where users can view a menu, place orders, and receive receipts. You'll be working with Python functions, lists, dictionaries, and loops to manage cookie orders and display information.

1. Begin by defining the function `add_cookie`. 

This function adds a new cookie to the menu. It takes a list, `menu`, and a dictionary with the cookie's `name` and `price` as parameters. When the `add_cookie` function is called, it should add the input cookie `name` and input `price` to the input menu. The function should mutate the `menu` object and should not return anything. 

Here is an example usage of the function: 

~~~   
>>> menu = []
>>> add_cookie(menu, "Chocolate Chip", 2.50)
>>> add_cookie(menu, "Oatmeal Raisin", 2.00)
>>> print(menu)
[{'name': 'Chocolate Chip', 'price': 2.5}, {'name': 'Oatmeal Raisin', 'price': 2.0}]
~~~

2. Define the function `display_menu`.

This function prints out the current menu of cookies by printing the element of an input `menu`. The function prints a header "Menu:" followed by a numbered list of cookies. Each item in the menu is displayed with its position in the list, name, and price. 

Here is an example usage of the function: 

~~~   
>>> menu = []
>>> add_cookie(menu, "Chocolate Chip", 2.50)
>>> add_cookie(menu, "Oatmeal Raisin", 2.00)
>>> print(menu)
[{'name': 'Chocolate Chip', 'price': 2.5}, {'name': 'Oatmeal Raisin', 'price': 2.0}]
>>> display_menu(menu)
Menu:
1. Chocolate Chip - $2.50
2. Oatmeal Raisin - $2.00
~~~

3. Define the function `take_order`.

Before you begin to implement this function, here is an overview of how it should work. The `take_order` function handles the process of taking an order from the user. It prompts for the user's name and the date, then displays the menu and allows the user to select cookies and their quantities. It also includes an option to remove items from the order and finally displays a receipt.

Here is an overview of how the function should work: 

~~~
>>> menu = []
>>> add_cookie(menu, "Chocolate Chip", 2.50)
>>> add_cookie(menu, "Oatmeal Raisin", 2.00)
>>> take_order(menu)
Enter your name: Viktorya
Enter the date (mm-dd-yyyy): 08-16-2024
Menu:
1. Chocolate Chip - $2.50
2. Oatmeal Raisin - $2.00
3. Strawberry Cake - $3.50
4. Cinnamon Crunch - $2.95
Choose a cookie number (1-4) or 0 to finish: 1
How many Chocolate Chip cookies do you want? 1
Choose a cookie number (1-4) or 0 to finish: 3
How many Strawberry Cake cookies do you want? 2
Choose a cookie number (1-4) or 0 to finish: 4
How many Cinnamon Crunch cookies do you want? 1
Choose a cookie number (1-4) or 0 to finish: 0
Viktorya, you ordered the following on 08-16-2024: {'Chocolate Chip': 1, 'Strawberry Cake': 2, 'Cinnamon Crunch': 1}
~~~

To begin, the `take_order` function should store the details of an order in a dictionary. To do this, instantiate a variable `order` to an empty dictionary. It should then prompt the user for their `name` and the `date` that they wish to make the order. Once this information is collected, the menu should be displayed. Should we simply use the `print` function? Why or why not? 

After displaying the menu, enter a loop to take cookie orders from the user. Initialize a variable choice with a value of 1 to start the loop. Inside the loop:
1. Ask the user to choose a cookie number from the menu. Ensure the user can also enter 0 to finish the ordering process.

2. Check if the chosen number is within the valid range of cookie numbers. If the choice is valid, proceed with the order. If not, print an error message and prompt the user again.

3. Retrieve the cookie details from the menu list based on the user's choice. Ask the user for the quantity they want to order. Update the `order` with this quantity. The cookie can either already be in `order` or not. What should we do in each case? 

After the user finishes ordering (by entering 0), we want to give the user a receipt. In order to do this, we will simplify print a message to the as seen in the above usage and highlighted below: 

~~~
Viktorya, you ordered the following on 08-16-2024: {'Chocolate Chip': 1, 'Strawberry Cake': 2, 'Cinnamon Crunch': 1}
~~~
