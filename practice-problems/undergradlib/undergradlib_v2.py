"""Simplified Mini Undergraduate Library Simulation!"""


class UndergraduateLibrary:
    books: dict[str, dict[str, int]]  # Dictionary of genres and available books.
    users: dict[str, list[str]]       # Dictionary of users and their checked-out items.

    def __init__(self, books: dict[str, dict[str, int]]) -> None:
        """
        Initialize the UndergraduateLibrary with books and and users.

        :param books: A dictionary containing genres as keys, and another dictionary as values. 
                      This dictionary maps book names to available copies.
        """
        self.books = books
        self.users = {}  # Initialize an empty dictionary for users

    def checkout_book(self) -> None:
        """Prompt user to check out a book from the library."""
        user = input("Enter your name: ")
        num_books_to_checkout = int(input("Enter the number of books you would like to checkout: "))
        num_books_checked_out = 0

        while num_books_checked_out < num_books_to_checkout:
            genre = input("Enter the genre of the book: ")
            book_name = input("Enter the name of the book to check out: ")

            if genre in self.books and book_name in self.books[genre]:
                if self.books[genre][book_name] > 0:
                    self.books[genre][book_name] -= 1

                    if user not in self.users:
                        self.users[user] = []
                    self.users[user].append(f"Book: '{book_name}' in Genre: '{genre}'")

                    print(f"Checked out '{book_name}'. Enjoy reading!")
                else:
                    print(f"Sorry, '{book_name}' is currently unavailable.")
            else:
                print(f"Sorry, '{book_name}' not found in {genre} genre.")

            num_books_checked_out += 1

    def search_user(self, user: str) -> None:
        """Search for a user and print their checked-out items."""
        if user in self.users:
            print(f"Items checked out by {user}:")
            for item in self.users[user]:
                print(f"- {item}")
        else:
            print(f"No records found for user '{user}'.")

    def __str__(self) -> str:
        """Return a string representation of the users and their checked-out items."""
        output = "Users and Checked-Out Items:\n"
        for user in self.users:
            output += f"User: {user}\n"
            for item in self.users[user]:
                output += f"  - {item}\n"
        return output

    def history_log(self) -> None:
        """
        Print a receipt of all checked-out books.
        """
        all_empty = True
        for user in self.users:
            items = self.users[user]
            if len(items) > 0:
                all_empty = False

        if all_empty:
            print("No items have been checked out.")
        else:
            print(self)  # Use the magic method __str__ for output


# Example Initialization
books = {
    "Fiction": {"The Great Gatsby": 5, "1984": 3},
    "Science": {"A Brief History of Time": 2, "The Selfish Gene": 4},
    "Technology": {"Clean Code": 1, "Design Patterns": 2},
    }

# Instantiate the library
library = UndergraduateLibrary(books)

# Example Usage
library.checkout_book()  # Prompts for user and book details
library.search_user("Viktorya")  # Searches for a user's checked-out items
library.history_log()        # Prints out a log of all checked-out items