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
Choose a cookie number (1-2) or 0 to finish: 1
How many Chocolate Chip cookies do you want? 1
Choose a cookie number (1-2) or 0 to finish: 2
How many Oatmeal Raisin cookies do you want? 3
Choose a cookie number (1-2) or 0 to finish: 0
Would you like to remove any items from your order? (yes/no): yes
Current Order:
Chocolate Chip: 1
Oatmeal Raisin: 3
Enter the name of the cookie you want to remove: Oatmeal Raisin
How many Oatmeal Raisin cookies would you like to remove? 1
---- Receipt: ----
Name: Viktorya
Date: 08-16-2024
1 x Chocolate Chip: $2.50
2 x Oatmeal Raisin: $4.00
Total: $6.50
__________________
~~~

To begin, the `take_order` function should store the details of an order in a dictionary. To do this, instantiate a variable `order` to an empty dictionary. It should then prompt the user for their `name` and the `date` that they wish to make the order. Once this information is collected, the menu should be displayed. Should we simply use the `print` function? Why or why not? 

After displaying the menu, enter a loop to take cookie orders from the user. Initialize a variable choice with a value of 1 to start the loop. Inside the loop:
1. Ask the user to choose a cookie number from the menu. Ensure the user can also enter 0 to finish the ordering process.

2. Check if the chosen number is within the valid range of cookie numbers. If the choice is valid, proceed with the order. If not, print an error message and prompt the user again.

3. Retrieve the cookie details from the menu list based on the user's choice. Ask the user for the quantity they want to order. Update the `order` with this quantity. The cookie can either already be in `order` or not. What should we do in each case? 

After the user finishes ordering (by entering 0), ask if they would like to remove any items from their order. If the user responds with "yes", we will want to remove the iteam they wish to remove. In order to simplify this, we will create `remove_item` function to handle this process. This function will take the `order` as it's input. 

    So if they respond with "yes", what should we do? Call the `remove_item` function. You should recieve a yellow squiggly line under `remove_item`. That's because we haven't defined the function yet! 

Finally, we want to give the user a receipt. In order to do this, we will simplify define a `show_receipt` function to display a detailed receipt of the order. We will call this function at the end of the `take_order` function. What information do you think a receipt should contain? The `show_receipt` function will take the `order`, `menu`, `name`, and `date` as inputs. Again, you should recieve a yellow squiggly line. 

4. Define the function `remove_item`.

The `remove_item` function allows users to remove items from their existing order. It interacts with the user to select which item to remove and how many to remove. The function also handles cases where the specified item is not in the order and allows the user to continue or stop removing items. As mentioned in step 3, the `remove_item` function will take take the `order` as it's input. The usage with context is in the example usage in step 3 but here is a highlighted version: 

~~~
Current Order:
Chocolate Chip: 1
Oatmeal Raisin: 3
Enter the name of the cookie you want to remove: Oatmeal Raisin
How many Oatmeal Raisin cookies would you like to remove? 1
~~~

Begin by instantiating a variable `condition` and assign it to `True`. Then set up a while loop where the condition is, `condition` == `True`. 

    You should then print the current state of the order, showing each item and its quantity. 

    Next, ask the user to input the name of the cookie they wish to remove or 'none' to exist. Verify if the specified item is present in the order. 
        If the item exists, request the number of cookies to remove. If the removal amount is greater than or equal to the current quantity, remove the item from the order. Otherwise, decrease the quantity by the removal amount.
        
        If item does not exist, this falls under the category of the the user either entering 'none' or non-existing cookie. If they entered 'none' we want to simply exist the program as we told the user above. If the user entered a non-existing cookie we want to print an error message indicating the item is not found in the order in the format seen in the example usage. We then want to ask the user if they want to continue removing items as in the example usage. What needs to happen in these scenarios? 

5. Define the function `show_receipt`. 

The show_receipt function is responsible for generating and displaying a detailed receipt for the user’s order. This includes showing the user’s name, the date of the order, a breakdown of the items ordered, and the total cost. As mentioned in step 3, the `show_receipt` function will take the `order`, `menu`, `name`, and `date` as inputs.

Here’s an overview of the the function: 
The function begins by printing a header for the receipt. It then prints each cookie's details and cost. Finally, the function calculates and prints the total cost of the order.

Here is an example usage of the function: 

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
Choose a cookie number (1-2) or 0 to finish: 1
How many Chocolate Chip cookies do you want? 1
Choose a cookie number (1-2) or 0 to finish: 2
How many Oatmeal Raisin cookies do you want? 3
Choose a cookie number (1-2) or 0 to finish: 0
Would you like to remove any items from your order? (yes/no): yes
Current Order:
Chocolate Chip: 1
Oatmeal Raisin: 3
Enter the name of the cookie you want to remove: Oatmeal Raisin
How many Oatmeal Raisin cookies would you like to remove? 1
---- Receipt: ----
Name: Viktorya
Date: 08-16-2024
1 x Chocolate Chip: $2.50
2 x Oatmeal Raisin: $4.00
Total: $6.50
__________________
~~~

* Notice that we do not call `show_receipt` directly. It is instead called within the `take_order` function. 

Start by printing a header, `"---- Receipt: ----"`, to indicate the beginning of the receipt. Print the user's `name` and the `date` of the order as formatted in the example usage. Create a variable `total` and initialize it to 0 to keep track of the total cost of the order. Obtain each cookie in the `order`. For each cookie in the `order`, find it in the `menu` to obtain the cookie details (name and price). Compute the cost for the ordered quantity of the cookie. Add this cost to the total. Print the quantity and cost of the item in the format specified above. 

After processing all items, print the total cost of the order. Print a footer line, `"__________________"`, to end the receipt.


