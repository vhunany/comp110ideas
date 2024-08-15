## UndergraduateLibrary

#### This simplified library simulation program is designed to help you understand and practice managing a small system that keeps track of book checkouts by users. You'll be working with Python classes, dictionaries, and user input. The provided code simulates a basic library system where students can check out books, and the library can keep track of who has checked out which books.

1. Begin by defining the class `UndergraduateLibrary`. The class should have 2 attributes: 

~~~   
books: dict[str, dict[str, int]]  # Dictionary of genres and available books.
users: dict[str, list[str]]       # Dictionary of users and their checked-out items.
~~~

Define the constructor. The constructor should take in a dictionary of books as a parameter and assign it to the books attribute. The users attribute should be initialized as an empty dictionary.


2. Instantiate your class and books. 

Below your class definition, instantiate a variable `books`. This books object is a `dict[str, dict[str, int]]`. Assign the `books` variable to the following: 

~~~
books = {
    "Fiction": {"The Great Gatsby": 5, "1984": 3},
    "Science": {"A Brief History of Time": 2, "The Selfish Gene": 4},
    "Technology": {"Clean Code": 1, "Design Patterns": 2},
}
~~~

Now, instantiate a class object `library` by calling the `UndergraduateLibrary` constructor. It should take in the `books` variable you defined earlier.

3. Create the `checkout_book` Method:

Define a method named `checkout_book` that allows users to check out one or more books.
This method should prompt the user for their name, the number of books they want to check out, the genre of each book, and the book title.
While the user still has books to request, your code should check that a requested book is available (i.e., its count is greater than zero). If it is, update the books dictionary to reflect the checkout and add the book to the user's list in the users dictionary.
If the book is not available or doesn't exist, print an appropriate message.

Here are example usages with example messages to print: 

<img src="Assets/checkout_book_ex.png" width=440 height=320>

<img src="Assets/checkout_book_none.png" width=440 height=320>

4. Create the `search_user` Method:

Define a method named search_user that takes in a user's name as a parameter.
This method should print out all the books that the user has checked out. 
If the user has no checked-out books, print a message indicating that no records were found.

Here are example usages: 

<img src="Assets/user_books_ex.png" width=440 height=320>

<img src="Assets/user_books_none.png" width=440 height=320>

5. Create the `__str__` method: 

Before you begin, here is an idea of how the method works: 

The `__str__` method in the UndergraduateLibrary class is designed to create a human-readable summary of the current state of the library, particularly focusing on which users have checked out which books. This method doesn't change any data in the object; it simply formats and returns a string that represents the object’s data in a clear and organized way.

What the `__str__` Method is Trying to Print:

The method is intended to print a list of all users who have checked out books, along with the titles and genres of the books they’ve checked out.

The output should look something like this:

~~~
Users and Checked-Out Items:
User: Alice
  - Book: '1984' in Genre: 'Fiction'
  - Book: 'Clean Code' in Genre: 'Technology'
User: Bob
  - Book: 'The Great Gatsby' in Genre: 'Fiction'
~~~

In this example, the method shows:
Each user’s name.
The books that user has checked out, with the book titles and their corresponding genres listed underneath the user’s name.

Start by creating a string variable output that will store the final formatted string. Begin with a header to introduce the information:

~~~
output = "Users and Checked-Out Items:\n"
~~~

This line initializes output with a message indicating that the following details pertain to users and their checked-out items. The `\n` ensures that any following details start on a new line (you don't need to worry too much about this, it simply just indents to a new line).

Then, iterate over users. By iterating over it, you can access each user and their corresponding list of borrowed books. 

For each user, append their name to the output string like so:

~~~
output += f"User: {user}\n"
~~~

Now for each user, you must obtain their checked-out items. Each items should then be appended to the output string, preceded by a dash and properly indented, as so:

~~~
output += f"  - {item}\n"
~~~

Once all the users and their books are added to the string, return the final string.

6. Create the `history_log` Method:

Before you begin, here is an idea of how the method is works: 
It is intended to print a complete log of all the users and the books they have checked out.
If no books have been checked out by any user, the method should print a message like:

~~~
No items have been checked out.
~~~

If books have been checked out, the method should print a detailed list similar to the output of the `__str__` method. For example:

~~~
Users and Checked-Out Items:
User: Alice
  - Book: '1984' in Genre: 'Fiction'
  - Book: 'Clean Code' in Genre: 'Technology'
User: Bob
  - Book: 'The Great Gatsby' in Genre: 'Fiction'
How to Implement This:
~~~

Begin by Checking if Any Books are Checked Out:

Start by checking whether the users dictionary has any entries. This dictionary keeps track of all users and their checked-out books.
If the dictionary is empty (meaning no users have checked out any books), simply print "No items have been checked out.".
Print the Checkout Log:

If there are users with checked-out books, call the `__str__` method to generate the detailed string representation of the current state of the library.
Print the string returned by `__str__`, which will display all users and the books they have borrowed.

[Solutions](#undergradlib_v2)